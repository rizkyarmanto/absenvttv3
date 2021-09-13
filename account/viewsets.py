import absen
import re
from account.models import *
from account.serializers import *
from rest_framework.parsers import JSONParser
from rest_framework import viewsets
from rest_framework.generics import ListAPIView
from rest_framework.authentication import TokenAuthentication
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework.views import APIView
from pusher import Pusher
from django.http import JsonResponse, HttpResponse
from django.views.decorators.csrf import csrf_exempt


# Create your views here.

pusher = Pusher(
  app_id='1264040',
  key='9c4a66de751481d7442a',
  secret='2723968367aaba3a1f2f',
  cluster='ap1',
  ssl=True
)

# ViewSets define the view behavior.
class MasterSiswaViewSet(viewsets.ModelViewSet):
    queryset = MasterSiswa.objects.all()
    serializer_class = MasterSiswaSerializer
    # authentication_classes = (TokenAuthentication,)
    # permission_classes = (IsAuthenticated,)

class MasterKelasViewSet(viewsets.ModelViewSet):
    queryset = MasterKelas.objects.all()
    serializer_class = MasterKelasSerializer
    # authentication_classes = (TokenAuthentication,)
    # permission_classes = (IsAuthenticated,)

class MasterJurusanViewSet(viewsets.ModelViewSet):
    queryset = MasterJurusan.objects.all()
    serializer_class = MasterJurusanSerializer
    # authentication_classes = (TokenAuthentication,)
    # permission_classes = (IsAuthenticated,)

class AbsensiViewSet(viewsets.ModelViewSet):
    queryset = Absensi.objects.raw('SELECT account_absensi.daily, account_absensi.status, account_absensi.checked_in, account_absensi.checked_out, account_absensi.checkin, account_absensi.checkout, account_mastersiswa.name, account_mastersiswa.nisn FROM account_mastersiswa INNER JOIN account_absensi ON account_mastersiswa.nisn = account_absensi.id_absensi_id')
    serializer_class = AbsensiSerializer

    # authentication_classes = (TokenAuthentication,)
    # permission_classes = (IsAuthenticated,)

class DailyViewSet(viewsets.ModelViewSet):
    queryset = Absensi.objects.all()
    serializer_class = DailySerializer
    # authentication_classes = (TokenAuthentication,)
    # permission_classes = (IsAuthenticated,)

    def get_queryset(self):
        absensi = Absensi.objects.all()
        return absensi

    def retrieve(self, request, *args, **kwargs):
        params = kwargs
        print(params['pk'])
        date = Absensi.objects.filter(daily=params['pk'])
        serializer = DailySerializer(date, many=True)
        return Response (serializer.data)


class AbsensiAPIView(APIView):

    parser_classes = [JSONParser]

    def post(self, request):
        absensi = Absensi(id_absensi=request.data['id_absensi'], daily=request.data['daily'], status=request.data['status'], checked_in=request.data['checked_in'], 
                          checked_out=request.data['checked_out'], checkin=request.data['checkin'], checkout=request.data['checkout'])
        absensi.save()

        absensi = {
            'id_absensi': absensi.id_absensi,
            'daily': absensi.daily, 
            'status': absensi.status, 
            'checked_in': absensi.checked_in,
            'checked_out': absensi.checked_out,
            'checkin': absensi.checkin,
            'checkout': absensi.checkout,
          }
        pusher.trigger('absenvttv3', 'absen', absensi)

        # return a json response of the broadcasted messgae
        return JsonResponse(absensi, safe=False)


class AkunAPIView(APIView):
    def post(self, request):
        akun = Akun(nama=request.data['nama'], password=request.data['password']);
        akun.save()
        akun = {
            'nama': akun.nama,
            'password': akun.password, 
            }
        pusher.trigger('absenvttv3', 'absen', akun)

        # return a json response of the broadcasted messgae
        return JsonResponse(akun, safe=False)









    # def update(self, request, *args, **kwargs):
    #     account_object = self.get_object()
    #     data = request.data

    #     siswa_object = MasterSiswa.objects.get(name=data["name"])

    #     account_object.siswa_object         = siswa_object
    #     account_object.id_absensi           = data["id_absensi"]
    #     account_object.daily                = data["daily"]
    #     account_object.status               = data["status"]
    #     account_object.checkin              = data["checkin"]
    #     account_object.checkout             = data["checkout"]

    #     account_object.save()

    #     serializer = AbsensiSerializer(account_object)

    #     return Response(serializer.data)

    # def partial_update(self, request, *args, **kwargs):
    #     account_object = self.get_object()
    #     data = request.data

    #     try:
    #         siswa_object = MasterSiswa.objects.get(name=data["name"])
    #         account_object.siswa_object = siswa_object
    #     except KeyError:
    #         pass

    #     account_object.id_absensi = data.get("id_absensi", account_object.id_absensi)
    #     account_object.daily = data.get("daily", account_object.daily)
    #     account_object.status = data.get("status", account_object.status)
    #     account_object.checkin = data.get("checkin", account_object.checkin)
    #     account_object.checkout = data.get("checkout", account_object.checkout)


    #     account_object.save()

    #     serializer = AbsensiSerializer(account_object)

    #     return Response(serializer.data)