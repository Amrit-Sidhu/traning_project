from django.shortcuts import render
from django.http import HttpResponse
from .models import farmer_record
from .models import animal_record
from .models import vaccination
from .models import milk_record
from .models import deworming
from .models import questions
from .models import answer
import datetime
from datetime import date
from django.http import HttpResponseRedirect
from PIL import Image
from django.core.files.storage import FileSystemStorage


def index(request):

    return render(request, 'dairy_website/index.html')


def register(request):
    return render(request, 'dairy_website/registration.html')


def goto_login(request):
    return render(request, 'dairy_website/index.html')


def goto_feed(request):
    return render(request, 'dairy_website/feed_management.html')


def goto_cattle(request):
    return render(request, 'dairy_website/help.html')


def goto_milking_methods(request):
    return render(request, 'dairy_website/milking_methods.html')


def goto_economic(request):
    return render(request, 'dairy_website/economiv_character.html')


def goto_housing(request):
    return render(request, 'dairy_website/housing_methods.html')


def goto_help(request):
    return render(request, 'dairy_website/help.html')


def goto_one_animal_milk(request):
    if request.method == "POST":
        if request.session.has_key('n'):
            f = request.session['n']
        farmer_data = farmer_record.objects.all().filter(farmer_id=f)
        farmer_name = farmer_data[0].name
        a_id = request.POST["a_id"]
        print(a_id)
        one_animal_milk = milk_record.objects.filter(tag_no=a_id)
        context = {"one_animal_milk":one_animal_milk,"tag_number":a_id,"farmer_name":farmer_name}

        return render(request, 'dairy_website/one_animal_milk.html',context)
    return render(request, 'dairy_website/one_animal_milk.html',)


def goto_milk_divided(request):
    avg_list = []
    tag_list = []
    tag_numbers = milk_record.objects.all().filter(milk_quantity__lte = 20).values_list('tag_no', flat=True)
    for i in tag_numbers:
        milk_ = milk_record.objects.all().filter(tag_no=i).values_list('milk_quantity', flat=True)
        if i not in tag_list:
            avg = sum(milk_)
            avg_list.append(avg)
            print(avg,i)
            tag_list.append(i)
    if request.session.has_key('n'):
        f = request.session['n']
    farmer_data = farmer_record.objects.all().filter(farmer_id=f)
    farmer_name = farmer_data[0].name
    print(avg_list)
    print(tag_list)
    final = zip(avg_list,tag_list)
    context = {"avg_list":final,"farmer_name":farmer_name}
    return render(request, 'dairy_website/milk-divided.html',context)


def goto_milk_divided_40(request):
    avg_list = []
    tag_list = []
    if request.session.has_key('n'):
        f = request.session['n']
    farmer_data = farmer_record.objects.all().filter(farmer_id=f)
    farmer_name = farmer_data[0].name
    tag_numbers = milk_record.objects.all().filter(milk_quantity__gte = 40).values_list('tag_no', flat=True)
    for i in tag_numbers:
        milk_ = milk_record.objects.all().filter(tag_no=i).values_list('milk_quantity', flat=True)
        if i not in tag_list:
            avg = sum(milk_)
            avg_list.append(avg)
            print(avg,i)
            tag_list.append(i)
    print(avg_list)
    print(tag_list)
    final = zip(avg_list,tag_list)
    context = {"avg_list":final,"farmer_name":farmer_name}
    return render(request, 'dairy_website/milk-divided.html',context)


def goto_milk_divided_20(request):
    avg_list = []
    tag_list = []
    if request.session.has_key('n'):
        f = request.session['n']
    farmer_data = farmer_record.objects.all().filter(farmer_id=f)
    farmer_name = farmer_data[0].name
    tag_numbers = milk_record.objects.all().filter(milk_quantity__gte = 21, milk_quantity__lte = 40).values_list('tag_no', flat=True)
    for i in tag_numbers:
        milk_ = milk_record.objects.all().filter(tag_no=i).values_list('milk_quantity', flat=True)
        if i not in tag_list:
            avg = sum(milk_)
            avg_list.append(avg)
            print(avg,i)
            tag_list.append(i)
    print(avg_list)
    print(tag_list)
    final = zip(avg_list,tag_list)
    context = {"avg_list":final,"farmer_name":farmer_name}
    return render(request, 'dairy_website/milk-divided.html',context)


def goto_ask(request):
    global f
    que_data = questions.objects.all()
    ans_data = answer.objects.all()
    if request.session.has_key('n'):
        f = request.session['n']
    farmer_data = farmer_record.objects.all().filter(farmer_id=f)
    phone_number = farmer_data[0].phone_number
    farmer_name = farmer_data[0].name
    farm_name = farmer_data[0].farm_name

    context = {"que_data": que_data,"ans_data":ans_data,"farmer_name":farmer_name,"farm_name":farm_name,
               "phone_number":phone_number}
    return render(request, 'dairy_website/ask.html', context)


def goto_que_added(request):
    global f
    que_data = questions.objects.all()
    ans_data = answer.objects.all()
    if request.session.has_key('n'):
        f = request.session['n']
    farmer_data = farmer_record.objects.all().filter(farmer_id=f)
    phone_number = farmer_data[0].phone_number
    farmer_name = farmer_data[0].name
    farm_name = farmer_data[0].farm_name

    context = {"que_data": que_data,"ans_data":ans_data,"farmer_name":farmer_name,"farm_name":farm_name,
               "phone_number":phone_number,"greetings":"your question is posted successfully..."}
    return render(request, 'dairy_website/ask.html', context)

def goto_ans_added(request):
    global f
    que_data = questions.objects.all()
    ans_data = answer.objects.all()
    if request.session.has_key('n'):
        f = request.session['n']
    farmer_data = farmer_record.objects.all().filter(farmer_id=f)
    phone_number = farmer_data[0].phone_number
    farmer_name = farmer_data[0].name
    farm_name = farmer_data[0].farm_name

    context = {"que_data": que_data,"ans_data":ans_data,"farmer_name":farmer_name,"farm_name":farm_name,
               "phone_number":phone_number,"greetings":"your answer is posted successfully..."}
    return render(request, 'dairy_website/ask.html', context)


def goto_regitration(request):
    return render(request, 'dairy_website/registration.html')


def goto_home(request):
    if request.session.has_key('n'):
        f = request.session['n']
        farmer_data = farmer_record.objects.all().filter(farmer_id=f)
        farmer_name = farmer_data[0].name

        context = {"farmer_name":farmer_name}
        return render(request, 'dairy_website/home.html',context)


def goto_animal_record(request):
    if request.session.has_key('n'):
        farmer_id = request.session['n']
        all_animal_quick_data = animal_record.objects.all().filter(farmer_id=farmer_id)
        total = len(animal_record.objects.all().filter(farmer_id=farmer_id)    )
        cow = len(animal_record.objects.all().filter(animal_type_age="cow",farmer_id=farmer_id))
        hiefer = len(animal_record.objects.all().filter(animal_type_age="hiefer",farmer_id=farmer_id))
        calf = len(animal_record.objects.all().filter(animal_type_age="calf",farmer_id=farmer_id))
        print(cow,calf,hiefer,total)
        farmer_id = request.session['n']
        farmer_data = farmer_record.objects.all().filter(farmer_id=farmer_id)
        farmer_name = farmer_data[0].name
        context = {"all_animal_quick_data": all_animal_quick_data,"total":total,"cow":cow,"calf":calf,"hiefer":hiefer,
                   "farmer_name": farmer_name}
        return render(request, 'dairy_website/animal_record.html', context)
    else:
        return render(request, 'dairy_website/index.html')


def goto_animal_added(request):
    if request.session.has_key('n'):
        farmer_id = request.session['n']
        farmer_data = farmer_record.objects.all().filter(farmer_id=farmer_id)
        farmer_name = farmer_data[0].name
        all_animal_quick_data = animal_record.objects.all()
        total = len(animal_record.objects.all())
        cow = len(animal_record.objects.all().filter(animal_type_age="cow"))
        hiefer = len(animal_record.objects.all().filter(animal_type_age="hiefer"))
        calf = len(animal_record.objects.all().filter(animal_type_age="calf"))
        print(cow, calf, hiefer, total)
        farmer_id = request.session['n']
        greetings = "congratulations!! your animal is added successfully..."
        context = {"all_animal_quick_data": all_animal_quick_data, "total": total, "cow": cow, "calf": calf,
                   "hiefer": hiefer,"greetings":greetings,"farmer_name":farmer_name}
        return render(request, 'dairy_website/animal_detail.html', context)


def goto_deworming_added(request):
    if request.session.has_key('n'):
        farmer_id = request.session['n']
        farmer_data = farmer_record.objects.all().filter(farmer_id=farmer_id)
        farmer_name = farmer_data[0].name
        all_animal_quick_data = animal_record.objects.all()

        greetings = "your data is saved successfully"
        context = {"all_animal_quick_data": all_animal_quick_data, "greetings":greetings,"farmer_name":farmer_name}
        return render(request, 'dairy_website/animal_detail.html', context)


def goto_animal_detail(request):
    farmer_id = request.session['n']
    farmer_data = farmer_record.objects.all().filter(farmer_id=farmer_id)
    farmer_name = farmer_data[0].name
    return render(request, 'dairy_website/animal_detail.html', {"farmer_name": farmer_name})


def goto_milk_record(request):
    if request.session.has_key('n'):
        farmer_id = request.session['n']
        farmer_data = farmer_record.objects.all().filter(farmer_id=farmer_id)
        farmer_name = farmer_data[0].name
        return render(request, 'dairy_website/milk_record.html',{"farmer_name":farmer_name})


def goto_update(request):
    if request.method == "POST":
        a_id = request.POST["a_id"]
        specific_animal_data = animal_record.objects.filter(tag_no=a_id)
        tag_no = specific_animal_data[0].tag_no
        animal_dob = specific_animal_data[0].animal_dob

        body_weight = specific_animal_data[0].body_weight
        breed_type = specific_animal_data[0].breed_type
        current_lactation = specific_animal_data[0].current_lactation
        last_calving_date = specific_animal_data[0].last_calving_date
        inseminated_type = specific_animal_data[0].inseminated_type
        bull_details = specific_animal_data[0].bull_details
        inseminated_date = specific_animal_data[0].inseminated_date
        animal_image = specific_animal_data[0].animal_image
        is_cattle_inseminated = specific_animal_data[0].is_cattle_inseminated

        brucellosis_d = vaccination.objects.filter(tag_no=a_id, vaccination_type="brucellosis")
        theileria_d = vaccination.objects.filter(tag_no=a_id, vaccination_type="theileria")
        haemorhaggic_speticaemia_d = vaccination.objects.filter(tag_no=a_id,
                                                                vaccination_type="haemorhaggic speticaemia")
        black_quarter_d = vaccination.objects.filter(tag_no=a_id, vaccination_type="black quarter")
        foot_and_mouth_disease_d = vaccination.objects.filter(tag_no=a_id, vaccination_type="foot and mouth disease")

        theileria_date = "not stored"
        theileria_due_date = "not stored"
        brucellosis_date = "not stored"
        brucellosis_due_date = "not stored"
        haemorhaggic_speticaemia_date = "not stored"
        haemorhaggic_speticaemia_due_date = "not stored"
        black_quarter_date = "not stored"
        black_quarter_due_date = "not stored"
        foot_and_mouth_disease_date = "not stored"
        foot_and_mouth_disease_due_date = "not stored"

        if theileria_d:
            theileria_date = theileria_d[0].vaccination_date
            theileria_due_date = theileria_d[0].due_date
        if haemorhaggic_speticaemia_d:
            haemorhaggic_speticaemia_date = haemorhaggic_speticaemia_d[0].vaccination_date
            haemorhaggic_speticaemia_due_date = haemorhaggic_speticaemia_d[0].due_date
        if black_quarter_d:
            black_quarter_date = black_quarter_d[0].vaccination_date
            black_quarter_due_date = black_quarter_d[0].due_date
        if foot_and_mouth_disease_d:
            foot_and_mouth_disease_date = foot_and_mouth_disease_d[0].vaccination_date
            foot_and_mouth_disease_due_date = foot_and_mouth_disease_d[0].due_date

        if brucellosis_d:
            brucellosis_date = brucellosis_d[0].vaccination_date
            brucellosis_due_date = brucellosis_d[0].due_date
        deworming_data = deworming.objects.filter(tag_no=a_id)

        medicine = "None"
        deworming_on = "None"
        deworming_due = "None"
        if deworming_data:
            medicine = deworming_data[0].medicine_name
            deworming_due= deworming_data[0].due_date
            deworming_on = deworming_data[0].deworming_date
        context = {"tag_no": tag_no, "animal_dob": animal_dob, "body_weight": body_weight, "breed_type": breed_type,
                   "current_lactation": current_lactation, "last_calving_date": last_calving_date, "inseminated_type":
                    inseminated_type, "bull_details": bull_details, "inseminated_date": inseminated_date,
                   "animal_image": animal_image, "brucellosis_date": brucellosis_date, "brucellosis_due_date"
                   : brucellosis_due_date, "theileria_date": theileria_date, "theileria_due_date": theileria_due_date,
                   "haemorhaggic_speticaemia_date": haemorhaggic_speticaemia_date, "haemorhaggic_speticaemia_due_date":
                       haemorhaggic_speticaemia_due_date, "black_quarter_date": black_quarter_date,
                   "black_quarter_due_date":black_quarter_due_date, "foot_and_mouth_disease_date": foot_and_mouth_disease_date,
                   "foot_and_mouth_disease_due_date": foot_and_mouth_disease_due_date,"medicine":medicine,
                   "deworming_on":deworming_on,"deworming_due":deworming_due,"is_cattle_inseminated":is_cattle_inseminated}
        return render(request, 'dairy_website/update_detail.html',context)


def goto_more_detail(request):
    if request.method == "POST":
        a_id = request.POST["a_id"]
        tag_numbers = animal_record.objects.all().values_list('tag_no', flat=True)
        farmer_id = request.session['n']
        farmer_data = farmer_record.objects.all().filter(farmer_id=farmer_id)
        farmer_name = farmer_data[0].name

        if a_id not in tag_numbers:
            all_animal_quick_data = animal_record.objects.all().filter(farmer_id=farmer_id)
            total = len(animal_record.objects.all().filter(farmer_id=farmer_id))
            cow = len(animal_record.objects.all().filter(animal_type_age="cow",farmer_id=farmer_id))
            hiefer = len(animal_record.objects.all().filter(animal_type_age="hiefer",farmer_id=farmer_id))
            calf = len(animal_record.objects.all().filter(animal_type_age="calf",farmer_id=farmer_id))
            print(cow, calf, hiefer, total)
            farmer_id = request.session['n']
            farmer_data = farmer_record.objects.all().filter(farmer_id=farmer_id)
            farmer_name = farmer_data[0].name

            context = {"all_animal_quick_data": all_animal_quick_data, "total": total, "cow": cow, "calf": calf,
                       "hiefer": hiefer,"farmer_name": farmer_name,"error": "Please enter a valid tag number"}
            return render(request, 'dairy_website/animal_record.html', context)
        else:
            specific_animal_data = animal_record.objects.filter(tag_no=a_id)
            tag_no = specific_animal_data[0].tag_no
            animal_dob = specific_animal_data[0].animal_dob
            body_weight = specific_animal_data[0].body_weight
            breed_type = specific_animal_data[0].breed_type
            current_lactation = specific_animal_data[0].current_lactation
            last_calving_date = specific_animal_data[0].last_calving_date
            inseminated_type = specific_animal_data[0].inseminated_type
            bull_details = specific_animal_data[0].bull_details
            inseminated_date = specific_animal_data[0].inseminated_date
            animal_image = specific_animal_data[0].animal_image

            brucellosis_d = vaccination.objects.filter(tag_no=a_id, vaccination_type="brucellosis")
            theileria_d = vaccination.objects.filter(tag_no=a_id, vaccination_type="theileria")
            haemorhaggic_speticaemia_d = vaccination.objects.filter(tag_no=a_id,
                                                                    vaccination_type="haemorhaggic speticaemia")
            black_quarter_d = vaccination.objects.filter(tag_no=a_id, vaccination_type="black quarter")
            foot_and_mouth_disease_d = vaccination.objects.filter(tag_no=a_id, vaccination_type="foot and mouth disease")

            theileria_date = "not stored"
            theileria_due_date = "not stored"
            brucellosis_date = "not stored"
            brucellosis_due_date = "not stored"
            haemorhaggic_speticaemia_date = "not stored"
            haemorhaggic_speticaemia_due_date = "not stored"
            black_quarter_date = "not stored"
            black_quarter_due_date = "not stored"
            foot_and_mouth_disease_date = "not stored"
            foot_and_mouth_disease_due_date = "not stored"

            if theileria_d:
                theileria_date = theileria_d[0].vaccination_date
                theileria_due_date = theileria_d[0].due_date
            if haemorhaggic_speticaemia_d:
                haemorhaggic_speticaemia_date = haemorhaggic_speticaemia_d[0].vaccination_date
                haemorhaggic_speticaemia_due_date = haemorhaggic_speticaemia_d[0].due_date
            if black_quarter_d:
                black_quarter_date = black_quarter_d[0].vaccination_date
                black_quarter_due_date = black_quarter_d[0].due_date
            if foot_and_mouth_disease_d:
                foot_and_mouth_disease_date = foot_and_mouth_disease_d[0].vaccination_date
                foot_and_mouth_disease_due_date = foot_and_mouth_disease_d[0].due_date

            if brucellosis_d:
                brucellosis_date = brucellosis_d[0].vaccination_date
                brucellosis_due_date = brucellosis_d[0].due_date
            deworming_data = deworming.objects.filter(tag_no=a_id)

            medicine = "None"
            deworming_on = "None"
            deworming_due = "None"
            if deworming_data:
                medicine = deworming_data[0].medicine_name
                deworming_due= deworming_data[0].due_date
                deworming_on = deworming_data[0].deworming_date
            context = {"tag_no": tag_no, "animal_dob": animal_dob, "body_weight": body_weight, "breed_type": breed_type,
                       "current_lactation": current_lactation, "last_calving_date": last_calving_date, "inseminated_type":
                           inseminated_type, "bull_details": bull_details, "inseminated_date": inseminated_date,
                       "animal_image": animal_image, "brucellosis_date": brucellosis_date, "brucellosis_due_date"
                       : brucellosis_due_date, "theileria_date": theileria_date, "theileria_due_date": theileria_due_date,
                       "haemorhaggic_speticaemia_date": haemorhaggic_speticaemia_date, "haemorhaggic_speticaemia_due_date":
                           haemorhaggic_speticaemia_due_date, "black_quarter_date": black_quarter_date,
                       "black_quarter_due_date":
                           black_quarter_due_date, "foot_and_mouth_disease_date": foot_and_mouth_disease_date,
                       "foot_and_mouth_disease_due_date": foot_and_mouth_disease_due_date,"medicine":medicine,
                       "deworming_on":deworming_on,"deworming_due":deworming_due,"farmer_name": farmer_name}

        return render(request, 'dairy_website/more_detail.html', context)


def add_farmer_data_in_database(request):
    if request.method == "POST":
        name = request.POST["name"]
        phone_number = request.POST["phone_number"]
        password = request.POST["password"]
        email = request.POST["email"]
        total_animal = request.POST["total_animal"]
        farm_name = request.POST["farm_name"]
        animal_type = request.POST["animal_type"]

        farmer_data = farmer_record(name=name, phone_number=phone_number, password=password, email=email, total_animal=
        total_animal, farm_name=farm_name, farm_type=animal_type)
        farmer_data.save()
        data = farmer_record.objects.all().filter(name=name)
        request.session['n'] = data[0].farmer_id
        f = request.session['n']
        farmer_data = farmer_record.objects.filter(farmer_id=f)
        farmer_name = farmer_data[0].name
        context = {"farmer_name": farmer_name}
        return render(request, 'dairy_website/home.html', context)


def show_username(request):
    if request.method == "POST":

        username_ = request.POST['username']
        password_ = request.POST['password']
        data = farmer_record.objects.all().filter(name=username_)
        context = {"name": username_, "password": password_}
        if len(data) == 0:
            context = {"error": "Invalid username !!", }
            return render(request, 'dairy_website/index.html', context)
        else:
            if data[0].name == username_ and data[0].password == password_:
                request.session['n'] = data[0].farmer_id
                f = request.session['n']
                farmer_data = farmer_record.objects.all().filter(farmer_id=f)
                farmer_name = farmer_data[0].name

                context = {"farmer_name": farmer_name}
                return render(request, 'dairy_website/home.html', context)
            else:
                context = {"error": "Please enter a valid password !!", }
                return render(request, 'dairy_website/index.html', context)


def add_animal_data_in_database(request):
    if request.method == "POST" and request.FILES['animal_image']:
        tag_no = request.POST["tag_number"]

        tag_numbers = animal_record.objects.all().values_list('tag_no', flat=True)
        farmer_id = request.session['n']
        farmer_data = farmer_record.objects.all().filter(farmer_id=farmer_id)
        farmer_name = farmer_data[0].name

        if tag_no in tag_numbers:
            context = {"farmer_name": farmer_name,"error": "This  tag number is already used"}
            return render(request, 'dairy_website/animal_detail.html', context)
        animal_dob = request.POST["animal_dob"]
        body_weight = request.POST["body_weight"]
        breed_type = request.POST["breed_type"]
        animal_image = request.FILES["animal_image"]

        animal_type_age = request.POST["animal_type_age"]
        farmer_id =  request.session['n']

        is_cattle_inseminated = "none"
        bull_details = "none"
        current_lactation = 0
        last_calving_date = "2000-01-01"
        inseminated_date = "2000-01-01"
        inseminated_type = "none"
        if animal_type_age != "calf":
            last_calving_date = request.POST["last_calving_date"]
            current_lactation = request.POST["current_lactation"]
            is_cattle_inseminated = request.POST["is_cattle_inseminated"]
            if is_cattle_inseminated == "yes":
                inseminated_type = request.POST["inseminated_type"]
                bull_details = request.POST["bull_details"]
                inseminated_date = request.POST["insemination_date"]

        fs = FileSystemStorage()
        image_name = fs.save(animal_image.name, animal_image)
        uploaded_image_url = fs.url(image_name)
        animal_dob_changed = datetime.datetime.strptime(animal_dob, "%Y-%m-%d").strftime("%Y-%m-%d")
        last_calving_date_changed = datetime.datetime.strptime(last_calving_date, "%Y-%m-%d").strftime("%Y-%m-%d")
        inseminated_date_changed = datetime.datetime.strptime(inseminated_date, "%Y-%m-%d").strftime("%Y-%m-%d")

        animal_data = animal_record(farmer_id=farmer_id, tag_no=tag_no, animal_dob=animal_dob_changed, body_weight=
                                    body_weight, breed_type=breed_type, current_lactation=current_lactation,
                                    last_calving_date=last_calving_date_changed, is_cattle_inseminated=
                                    is_cattle_inseminated, inseminated_type=inseminated_type, bull_details=bull_details,
                                    inseminated_date=inseminated_date_changed, animal_image=uploaded_image_url,
                                    animal_type_age=animal_type_age)
        animal_data.save()
        context = {"farmer_name":farmer_name}
        return HttpResponseRedirect("/dairy_website/goto_animal_added",context)
    else:
        return HttpResponse("error")


def add_vaccination_in_database(request):
    if request.session.has_key('n'):
        if request.method == "POST":
            tag_numbers = vaccination.objects.all().values_list('tag_no', flat=True)
            farmer_id = request.session['n']
            farmer_data = farmer_record.objects.all().filter(farmer_id=farmer_id)
            farmer_name = farmer_data[0].name
            tag_no = request.POST["tag_no"]
            tag_numbers_all = animal_record.objects.all().values_list('tag_no', flat=True)
            if tag_no not in tag_numbers_all:
                context = {"farmer_name": farmer_name, "vaccination_error": "This  tag number is not exist in your animal list"}
                return render(request, 'dairy_website/animal_detail.html', context)
            else:
                if tag_no in tag_numbers:
                    context = {"farmer_name": farmer_name,"vaccination_error": "This  tag number is already used"}
                    return render(request, 'dairy_website/animal_detail.html', context)
                else:
                    vaccination_type = request.POST["vaccination_type"]
                    vaccination_date = request.POST["vaccination_date"]
                    due_date = request.POST["due_date"]
                    vaccination_date = datetime.datetime.strptime(vaccination_date, "%Y-%m-%d").strftime("%Y-%m-%d")
                    due_date = datetime.datetime.strptime(due_date, "%Y-%m-%d").strftime("%Y-%m-%d")

                    f = request.session['n']
                    for_check_v = request.POST["for_check_v"]
                    print("for check",for_check_v)
                    if for_check_v == "yes":
                        all_animal = animal_record.objects.all().filter(farmer_id=farmer_id).values_list('tag_no',flat=True)
                        for i in all_animal:
                            vaccination_data = vaccination(tag_no=i, vaccination_type=vaccination_type,
                                                           vaccination_date=vaccination_date, due_date=due_date, farmer_id=f)
                            vaccination_data.save()
                        return HttpResponseRedirect("/dairy_website/goto_deworming_added")
                    else:
                        vaccination_data = vaccination(tag_no=tag_no, vaccination_type=vaccination_type,
                                                       vaccination_date=vaccination_date, due_date=due_date, farmer_id=f)
                        vaccination_data.save()
                        return HttpResponseRedirect("/dairy_website/goto_deworming_added")
    return render(request, 'dairy_website/index.html')


def add_deworming_in_database(request):
    if request.method == "POST":
        tag_no = request.POST["tag_no"]

        tag_numbers = deworming.objects.all().values_list('tag_no', flat=True)
        farmer_id = request.session['n']
        farmer_data = farmer_record.objects.all().filter(farmer_id=farmer_id)
        farmer_name = farmer_data[0].name

        tag_numbers_all = animal_record.objects.all().values_list('tag_no', flat=True)
        if tag_no not in tag_numbers_all:
            context = {"farmer_name": farmer_name,
                       "de_error": "This  tag number is not exist in your animal list"}
            return render(request, 'dairy_website/animal_detail.html', context)
        else:
            if tag_no in tag_numbers:
                context = {"farmer_name": farmer_name, "de_error": "This tag number is already used"}
                return render(request, 'dairy_website/animal_detail.html', context)
            else:
                deworming_date = request.POST["deworming_date"]
                due_date = request.POST["due_date"]
                medicine_name = request.POST["medicine_name"]
                f = request.session['n']
                deworming_date = datetime.datetime.strptime(deworming_date, "%Y-%m-%d").strftime("%Y-%m-%d")
                due_date = datetime.datetime.strptime(due_date, "%Y-%m-%d").strftime("%Y-%m-%d")

                for_check_de = request.POST["for_check_de"]
                if for_check_de == "yes":
                    all_animal = animal_record.objects.all().values_list('tag_no',flat=True)
                    for i in all_animal:
                        deworming_data = deworming(tag_no=i, deworming_date=deworming_date, due_date=due_date, farmer_id=f,
                                                   medicine_name=medicine_name)
                        deworming_data.save()
                    return HttpResponseRedirect("/dairy_website/goto_deworming_added")
                else:
                    deworming_data = deworming(tag_no=tag_no, deworming_date=deworming_date, due_date=due_date, farmer_id=f,
                                               medicine_name=medicine_name)
                    deworming_data.save()
                    return HttpResponseRedirect("/dairy_website/goto_deworming_added")


def add_milk_data_in_database(request):

    if request.method == "POST":
        farmer_id = request.session['n']
        farmer_data = farmer_record.objects.all().filter(farmer_id=farmer_id)
        farmer_name = farmer_data[0].name
        tag_no = request.POST["tag_no"]
        milk_time = request.POST["milk_time"]
        milk_quantity = request.POST["milk_quantity"]
        milk_date = request.POST["milk_date"]
        f = request.session['n']
        milk_date = datetime.datetime.strptime(milk_date, "%Y-%m-%d").strftime("%Y-%m-%d")
        tag_numbers = animal_record.objects.all().values_list('tag_no', flat=True)
        if tag_no in tag_numbers:
            milk_data = milk_record(tag_no=tag_no, milk_time=milk_time, milk_quantity=milk_quantity, milk_date=milk_date
                                    , farmer_id=f)
            milk_data.save()
            context = { "farmer_name": farmer_name,"greetings":"your data is saved sucessfully..."}
            return render(request, 'dairy_website/milk_record.html', context)
        else:
            context = {"error":"Please enter a valid tag number", "farmer_name":farmer_name}
            return render(request, 'dairy_website/milk_record.html',context)


def add_que_in_database(request):
    if request.method == "POST":
        que_subject = request.POST['que_subject']
        que_body = request.POST['que_body']
        farmer_id_que = request.session['n']
        que_date = datetime.date.today()
        data = farmer_record.objects.all().filter(farmer_id=farmer_id_que)
        farmer_name_que = data[0].name
        q = questions(farmer_id_que=farmer_id_que, que_body=que_body, que_subject=que_subject, que_date=que_date,
                      farmer_name_que=farmer_name_que)
        q.save()
        que_data = questions.objects.all()

        context = {"que_data": que_data}
        return HttpResponseRedirect("/dairy_website/goto_que_added")
    return render(request, 'dairy_website/ask.html')


def add_ans_in_database(request):
    if request.method == "POST":
        ans_body = request.POST['ans_body']
        farmer_id_ans = request.session['n']
        ans_date = datetime.date.today()
        data = farmer_record.objects.all().filter(farmer_id=farmer_id_ans)
        farmer_name_ans = data[0].name

        que_id = request.POST['que_id']
        q = answer(farmer_id_ans=farmer_id_ans, ans_body=ans_body, ans_date=ans_date, farmer_name_ans=farmer_name_ans,
                   que_id=que_id)
        q.save()
        return HttpResponseRedirect("/dairy_website/goto_ans_added")

def show_answer(request):
    if request.method == "POST":
        que_id_for_ans = request.POST['que_id_for_ans']
        global f
        one_que_data = questions.objects.all().filter(que_id=que_id_for_ans)
        one_ans_data = answer.objects.all().filter(que_id=que_id_for_ans)

        context = {"one_ans_data":one_ans_data,"one_que_data":one_que_data}
        if one_ans_data:
            return render(request, 'dairy_website/ask.html', context)
        else:

            '''que_data = questions.objects.all()
            if request.session.has_key('n'):
                f = request.session['n']
            farmer_data = farmer_record.objects.all().filter(farmer_id=f)
            phone_number = farmer_data[0].phone_number
            farmer_name = farmer_data[0].name
            farm_name = farmer_data[0].farm_name
            ans_data = answer.objects.all()
            
            context = {"que_data": que_data, "ans_data": ans_data, "farmer_name": farmer_name, "farm_name": farm_name,
                      "phone_number": phone_number}
            return render(request, 'dairy_website/ask.html', context)'''

        return HttpResponseRedirect("/dairy_website/goto_ask")


def update_animal_data_in_database(request):
    if request.method == "POST":
        tag_no = request.POST["tag_number"]
        animal_dob = request.POST["animal_dob"]
        body_weight = request.POST["body_weight"]
        breed_type = request.POST["breed_type"]
        animal_type_age = request.POST["animal_type_age"]
        farmer_id = request.session['n']
        due_date = request.POST["due_date"]
        medicine_name = request.POST["medicine_name"]

        theileria_date = request.POST["theileria_date"]
        theileria_due_date = request.POST["theileria_due_date"]
        th_data = vaccination.objects.all().filter(tag_no=tag_no,vaccination_type="theileria")
        f = request.session['n']
        if theileria_date:
            if th_data:
                theileria_date = datetime.datetime.strptime(theileria_date, "%Y-%m-%d").strftime("%Y-%m-%d")
                theileria_due_date = datetime.datetime.strptime(theileria_due_date, "%Y-%m-%d").strftime("%Y-%m-%d")
                th_data.update(vaccination_date=theileria_date,due_date=theileria_due_date)
            else:
                theileria_date = datetime.datetime.strptime(theileria_date, "%Y-%m-%d").strftime("%Y-%m-%d")
                theileria_due_date = datetime.datetime.strptime(theileria_due_date, "%Y-%m-%d").strftime("%Y-%m-%d")
                vaccination_data = vaccination(tag_no=tag_no, vaccination_type="theileria",
                                               vaccination_date=theileria_date, due_date=theileria_due_date, farmer_id=f)
                vaccination_data.save()

        haemorhaggic_speticaemia_date = request.POST["haemorhaggic_speticaemia_date"]
        haemorhaggic_speticaemia_due_date = request.POST["haemorhaggic_speticaemia_due_date"]
        hs_data = vaccination.objects.all().filter(tag_no=tag_no, vaccination_type="haemorhaggic speticaemia")

        if haemorhaggic_speticaemia_date:
            if hs_data:
                haemorhaggic_speticaemia_date = datetime.datetime.strptime(haemorhaggic_speticaemia_date,
                                                                           "%Y-%m-%d").strftime("%Y-%m-%d")
                haemorhaggic_speticaemia_due_date = datetime.datetime.strptime(haemorhaggic_speticaemia_due_date,
                                                                               "%Y-%m-%d").strftime("%Y-%m-%d")
                hs_data.update(vaccination_date=haemorhaggic_speticaemia_date, due_date=haemorhaggic_speticaemia_due_date)
            else:
                haemorhaggic_speticaemia_date = datetime.datetime.strptime(haemorhaggic_speticaemia_date, "%Y-%m-%d").strftime("%Y-%m-%d")
                haemorhaggic_speticaemia_due_date = datetime.datetime.strptime(haemorhaggic_speticaemia_due_date, "%Y-%m-%d").strftime("%Y-%m-%d")
                vaccination_data_hs = vaccination(tag_no=tag_no, vaccination_type="haemorhaggic speticaemia",
                                               vaccination_date=haemorhaggic_speticaemia_date, due_date=haemorhaggic_speticaemia_due_date, farmer_id=f)
                vaccination_data_hs.save()

        brucellosis_date = request.POST["brucellosis_date"]
        brucellosis_due_date = request.POST["brucellosis_due_date"]
        bl_data = vaccination.objects.all().filter(tag_no=tag_no, vaccination_type="brucellosis")

        if brucellosis_date:
            if bl_data:
                brucellosis_date = datetime.datetime.strptime(brucellosis_date, "%Y-%m-%d").strftime("%Y-%m-%d")
                brucellosis_due_date = datetime.datetime.strptime(brucellosis_due_date, "%Y-%m-%d").strftime("%Y-%m-%d")
                bl_data.update(vaccination_date=brucellosis_date, due_date=brucellosis_due_date)
            else:
                brucellosis_date = datetime.datetime.strptime(brucellosis_date, "%Y-%m-%d").strftime("%Y-%m-%d")
                brucellosis_due_date = datetime.datetime.strptime(brucellosis_due_date, "%Y-%m-%d").strftime("%Y-%m-%d")
                vaccination_data_b = vaccination(tag_no=tag_no, vaccination_type="brucellosis",
                                               vaccination_date=brucellosis_date, due_date=brucellosis_due_date, farmer_id=f)
                vaccination_data_b.save()

        black_quarter_date = request.POST["black_quarter_date"]
        black_quarter_due_date = request.POST["black_quarter_due_date"]
        bq_data = vaccination.objects.all().filter(tag_no=tag_no, vaccination_type="black quarter")
        if black_quarter_date:
            if bq_data:
                black_quarter_date = datetime.datetime.strptime(black_quarter_date, "%Y-%m-%d").strftime("%Y-%m-%d")
                black_quarter_due_date = datetime.datetime.strptime(black_quarter_due_date, "%Y-%m-%d").strftime("%Y-%m-%d")
                bq_data.update(vaccination_date=black_quarter_date, due_date=black_quarter_due_date)
            else:
                black_quarter_date = datetime.datetime.strptime(black_quarter_date, "%Y-%m-%d").strftime("%Y-%m-%d")
                black_quarter_due_date = datetime.datetime.strptime(black_quarter_due_date, "%Y-%m-%d").strftime("%Y-%m-%d")
                vaccination_data_bq = vaccination(tag_no=tag_no, vaccination_type="black quarter",
                                               vaccination_date=black_quarter_date, due_date=black_quarter_due_date,
                                               farmer_id=f)
                vaccination_data_bq.save()

        foot_and_mouth_disease_date = request.POST["foot_and_mouth_disease_date"]
        foot_and_mouth_disease_due_date = request.POST["foot_and_mouth_disease_due_date"]
        fmd_data = vaccination.objects.all().filter(tag_no=tag_no, vaccination_type="foot and mouth disease")

        if foot_and_mouth_disease_date:
            if fmd_data:
                foot_and_mouth_disease_date = datetime.datetime.strptime(foot_and_mouth_disease_date, "%Y-%m-%d").strftime("%Y-%m-%d")
                foot_and_mouth_disease_due_date = datetime.datetime.strptime(foot_and_mouth_disease_due_date, "%Y-%m-%d").strftime("%Y-%m-%d")
                fmd_data.update(vaccination_date=foot_and_mouth_disease_date, due_date=foot_and_mouth_disease_due_date)
            else:
                foot_and_mouth_disease_date = datetime.datetime.strptime(foot_and_mouth_disease_date, "%Y-%m-%d").strftime("%Y-%m-%d")
                foot_and_mouth_disease_due_date = datetime.datetime.strptime(foot_and_mouth_disease_due_date, "%Y-%m-%d").strftime("%Y-%m-%d")
                vaccination_data_fmd = vaccination(tag_no=tag_no, vaccination_type="foot and mouth disease",
                                               vaccination_date=foot_and_mouth_disease_date, due_date=foot_and_mouth_disease_due_date,
                                               farmer_id=f)
                vaccination_data_fmd.save()

        is_cattle_inseminated = "none"
        bull_details = "none"
        current_lactation = 0
        last_calving_date = "2000-01-01"
        inseminated_date = "2000-01-01"
        inseminated_type = "none"
        if animal_type_age != "calf":
            last_calving_date = request.POST["last_calving_date"]
            current_lactation = request.POST["current_lactation"]

            if is_cattle_inseminated == "yes":
                inseminated_type = request.POST["inseminated_type"]
                bull_details = request.POST["bull_details"]
                inseminated_date = request.POST["insemination_date"]
        animal_dob_changed = datetime.datetime.strptime(animal_dob, "%Y-%m-%d").strftime("%Y-%m-%d")
        last_calving_date_changed = datetime.datetime.strptime(last_calving_date, "%Y-%m-%d").strftime("%Y-%m-%d")
        inseminated_date_changed = datetime.datetime.strptime(inseminated_date, "%Y-%m-%d").strftime("%Y-%m-%d")
        animal_data = animal_record.objects.all().filter(tag_no=tag_no)

        animal_data.update(farmer_id= farmer_id, tag_no=tag_no, animal_dob=animal_dob_changed, body_weight=body_weight,
                           breed_type=breed_type, current_lactation=current_lactation,last_calving_date=
                           last_calving_date_changed, is_cattle_inseminated=is_cattle_inseminated, inseminated_type=
                           inseminated_type, bull_details=bull_details,inseminated_date=inseminated_date_changed)

        due_date = request.POST["due_date"]
        deworming_date = request.POST["deworming_date"]
        deworming_data = deworming.objects.all().filter(tag_no=tag_no)

        if deworming_date:
            if deworming_data:
                deworming_date = datetime.datetime.strptime(deworming_date,
                                                                           "%Y-%m-%d").strftime("%Y-%m-%d")
                due_date = datetime.datetime.strptime(due_date, "%Y-%m-%d").strftime("%Y-%m-%d")
                deworming_data.update(tag_no=tag_no, deworming_date=deworming_date, due_date=due_date, farmer_id=f,
                                      medicine_name=medicine_name)
            else:
                deworming_date = datetime.datetime.strptime(deworming_date, "%Y-%m-%d").strftime("%Y-%m-%d")
                due_date = datetime.datetime.strptime(due_date, "%Y-%m-%d").strftime("%Y-%m-%d")
                deworming_data_new = deworming(tag_no=tag_no, deworming_date=deworming_date, due_date=due_date,
                                               farmer_id=f,medicine_name=medicine_name)
                deworming_data_new.save()
        """data to be show in page"""
        specific_animal_data = animal_record.objects.filter(tag_no=tag_no)
        tag_no = specific_animal_data[0].tag_no
        animal_dob = specific_animal_data[0].animal_dob

        body_weight = specific_animal_data[0].body_weight
        breed_type = specific_animal_data[0].breed_type
        current_lactation = specific_animal_data[0].current_lactation
        last_calving_date = specific_animal_data[0].last_calving_date
        inseminated_type = specific_animal_data[0].inseminated_type
        bull_details = specific_animal_data[0].bull_details
        inseminated_date = specific_animal_data[0].inseminated_date
        animal_image = specific_animal_data[0].animal_image
        is_cattle_inseminated = specific_animal_data[0].is_cattle_inseminated

        brucellosis_d = vaccination.objects.filter(tag_no=tag_no, vaccination_type="brucellosis")
        theileria_d = vaccination.objects.filter(tag_no=tag_no, vaccination_type="theileria")
        haemorhaggic_speticaemia_d = vaccination.objects.filter(tag_no=tag_no,
                                                                vaccination_type="haemorhaggic speticaemia")
        black_quarter_d = vaccination.objects.filter(tag_no=tag_no, vaccination_type="black quarter")
        foot_and_mouth_disease_d = vaccination.objects.filter(tag_no=tag_no, vaccination_type="foot and mouth disease")

        theileria_date = "not stored"
        theileria_due_date = "not stored"
        brucellosis_date = "not stored"
        brucellosis_due_date = "not stored"
        haemorhaggic_speticaemia_date = "not stored"
        haemorhaggic_speticaemia_due_date = "not stored"
        black_quarter_date = "not stored"
        black_quarter_due_date = "not stored"
        foot_and_mouth_disease_date = "not stored"
        foot_and_mouth_disease_due_date = "not stored"

        if theileria_d:
            theileria_date = theileria_d[0].vaccination_date
            theileria_due_date = theileria_d[0].due_date
        if haemorhaggic_speticaemia_d:
            haemorhaggic_speticaemia_date = haemorhaggic_speticaemia_d[0].vaccination_date
            haemorhaggic_speticaemia_due_date = haemorhaggic_speticaemia_d[0].due_date
        if black_quarter_d:
            black_quarter_date = black_quarter_d[0].vaccination_date
            black_quarter_due_date = black_quarter_d[0].due_date
        if foot_and_mouth_disease_d:
            foot_and_mouth_disease_date = foot_and_mouth_disease_d[0].vaccination_date
            foot_and_mouth_disease_due_date = foot_and_mouth_disease_d[0].due_date

        if brucellosis_d:
            brucellosis_date = brucellosis_d[0].vaccination_date
            brucellosis_due_date = brucellosis_d[0].due_date
        deworming_data = deworming.objects.filter(tag_no=tag_no)

        medicine = "None"
        deworming_on = "None"
        deworming_due = "None"
        greetings = "your data is updated.."
        if deworming_data:
            medicine = deworming_data[0].medicine_name
            deworming_due = deworming_data[0].due_date
            deworming_on = deworming_data[0].deworming_date
        context = {"tag_no": tag_no, "animal_dob": animal_dob, "body_weight": body_weight, "breed_type": breed_type,
                   "current_lactation": current_lactation, "last_calving_date": last_calving_date, "inseminated_type":
                       inseminated_type, "bull_details": bull_details, "inseminated_date": inseminated_date,
                   "animal_image": animal_image, "brucellosis_date": brucellosis_date, "brucellosis_due_date"
                   : brucellosis_due_date, "theileria_date": theileria_date, "theileria_due_date": theileria_due_date,
                   "haemorhaggic_speticaemia_date": haemorhaggic_speticaemia_date, "haemorhaggic_speticaemia_due_date":
                       haemorhaggic_speticaemia_due_date, "black_quarter_date": black_quarter_date,
                   "black_quarter_due_date": black_quarter_due_date,
                   "foot_and_mouth_disease_date": foot_and_mouth_disease_date,
                   "foot_and_mouth_disease_due_date": foot_and_mouth_disease_due_date, "medicine": medicine,
                   "deworming_on": deworming_on, "deworming_due": deworming_due,
                   "is_cattle_inseminated": is_cattle_inseminated,"greetings":greetings}
        return render(request, 'dairy_website/more_detail.html', context)

    else:
        return HttpResponse("error")


def goto_re(request):
    if request.method == "POST":
        likes = request.POST["likes"]
        dislikes = request.POST["dislikes"]
        que_id = request.POST["que_id"]
        print("likes==",likes," ","dislikes=",dislikes,que_id)
        que_data = questions.objects.all().filter(que_id=que_id)
        que_data.update(likes=likes, dislikes=dislikes)
    return HttpResponse("")