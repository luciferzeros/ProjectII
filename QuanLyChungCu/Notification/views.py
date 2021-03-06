from django.db.models.functions import Coalesce
from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from .models import Notify, Notify_User
from django.contrib.auth.mixins import LoginRequiredMixin
from django.core.files.storage import FileSystemStorage
from django.views import View


class Index_Notify(LoginRequiredMixin, View):
    def get(self, request):
        if request.user.is_staff:
            notify = Notify.objects.filter(manage_id=request.user.id).order_by("-id")
            return render(request, 'index_notify_manage.html', {"notify": notify})
        else:
            notify = Notify_User.objects.filter(id_user=request.user.id).order_by("-id")
            return render(request, 'index_notify.html', {"notify": notify})


class Create_Notify(LoginRequiredMixin, View):
    def get(self, request):
        if request.user.is_staff:
            return render(request, 'create_notify.html')
        else:
            return redirect("index_notify")

    def post(selfs, request):
        if request.user.is_staff:
            try:
                notify = Notify()
                notify.manage_id = request.user
                notify.heading = request.POST["heading"]
                notify.content = request.POST["content"]
                if request.FILES['file']:
                    file = request.FILES['file']
                    filename = str(file)
                    if filename[len(filename) - 4:len(filename)] == '.pdf':
                        fs = FileSystemStorage()
                        filename = fs.save(file.name, file)
                        uploaded_file_url = fs.url(filename)
                        notify.file = uploaded_file_url
                notify.save()
                return redirect('send_notify', id=notify.id)
            except Exception as e:
                raise e
        else:
            return redirect('index_notify')


class Send_Notify(LoginRequiredMixin, View):
    def get(self, request, id):
        if request.user.is_staff:
            try:
                notify = Notify.objects.get(pk=id)
                noti_user = Notify_User.objects.filter(notify_id=notify)
                users = User.objects.filter(is_staff=False).exclude(id__in=noti_user.values_list("id_user", flat=True))
                return render(request, "send_notify.html", {'noti_user': noti_user, "notify": notify, "users": users})
            except Exception as e:
                raise e
        else:
            return redirect("index_notify")

    def post(self, request, id):
        if request.user.is_staff:
            try:
                notify = Notify.objects.get(pk=id)

                id_user = request.POST["user_notify"]
                if int(id_user) == 0:
                    noti_user = Notify_User.objects.filter(notify_id=notify)
                    users = User.objects.filter(is_staff=False).exclude(id__in=noti_user.values_list("id_user", flat=True))
                    for user in users:
                        notify_user = Notify_User()
                        notify_user.notify_id = notify
                        notify_user.id_user = user
                        notify_user.save()
                else:
                    notify_user = Notify_User()
                    notify_user.notify_id = notify
                    users = User.objects.get(pk=id_user)
                    notify_user.id_user = users
                    notify_user.save()
                noti_user = Notify_User.objects.filter(notify_id=notify)
                users = User.objects.filter(is_staff=False).exclude(id__in=noti_user.values_list("id_user", flat=True))
                return render(request, "send_notify.html", {'noti_user': noti_user, "notify": notify, "users": users})
            except Exception as e:
                raise e
        else:
            return redirect('index_notify')


class Edit_Notify(LoginRequiredMixin, View):
    def get(self, request, id):
        if request.user.is_staff:
            try:
                notify = Notify.objects.get(pk=id)
                return render(request, 'edit_notify.html', {'notify': notify})
            except Exception as e:
                return redirect("index_notify")
        else:
            return redirect("index_notify")


    def post(self, request, id):
        if request.user.is_staff:
            try:
                notify = Notify.objects.get(pk=id)
                notify.heading = request.POST['heading']
                notify.content = request.POST['content']
                if request.FILES['file']:
                    file = request.FILES['file']
                    filename = str(file)
                    if filename[len(filename) - 4:len(filename)] == '.pdf':
                        fs = FileSystemStorage()
                        filename = fs.save(file.name, file)
                        uploaded_file_url = fs.url(filename)
                        notify.file = uploaded_file_url
                notify.save()
                return redirect('send_notify', id=id)
            except Exception as e:
                raise e
                # return redirect("sos")
        else:
            return redirect("index_notify")


class Delete_notify(LoginRequiredMixin, View):
    def get(self, request, id):
        if request.user.is_staff:
            try:
                notify = Notify.objects.get(pk=id)
                notify.delete()
                return redirect("index_notify")
            except Exception as e:
                return redirect("index_notify")
        else:
            return redirect("index_notify")


class View_notify(LoginRequiredMixin, View):
    def get(self, request, id):
        if request.user.is_staff:
            return redirect("index_notify")
        else:
            try:
                notify = Notify_User.objects.filter(id_user=request.user, notify_id=id).first()
                content = notify.notify_id.content.split("\n")
                return render(request, "view_notify.html", {'notify': notify, 'content': content})
            except Exception as e:
                raise e








