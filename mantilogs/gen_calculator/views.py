from django.shortcuts import render, get_object_or_404, get_list_or_404
from django.http import HttpResponseRedirect
from django.template.defaulttags import register
from leopard_gecko import models as gecko_M

@register.filter
def get_item(dictionary, key):
    return dictionary.get(key)

# Create your views here.
def gecko_calc(request):
    '''
        Calculate the offspring of a gecko based on morphs, morph combos and their properties.
        This view should render a form that allows you to select the parents from the geckos available. 
        When you click submit it will render a partial from another view below the form showing possible morphs from the pair.
    '''
    geckos = gecko_M.Gecko.objects.all()
    context = {'user_info': request.user, 'geckos': geckos}
    return render(request, 'gecko_calc.html', context)

def gecko_partial(request,gecko1,gecko2):
    '''
        Gets the data from the gecko_calc form and retrieves the potential morphs as a list of links and images.
    '''
    gecko_one = gecko_M.Gecko.objects.filter(name=gecko1).last()
    gecko_two = gecko_M.Gecko.objects.filter(name=gecko2).last()
    gecko_one_morphs = gecko_one.morphs.all()
    gecko_two_morphs = gecko_two.morphs.all()
    parent_morphs = construct_morph_set(gecko_one_morphs, gecko_two_morphs)
    all_morphs = decon_morphs(parent_morphs).union(parent_morphs)
    all_morphs_pass_two = decon_morphs(all_morphs).union(all_morphs)
    potential_morphs = find_potential_morphs(all_morphs_pass_two).union(all_morphs_pass_two)
    all_potential_morphs = all_morphs_pass_two.union(potential_morphs)
    print(parent_morphs)
    print("=====================================")
    print(all_morphs)
    print("====================================")
    print(potential_morphs)
    print("====================================")
    print(all_potential_morphs)



    context = {'gecko1': gecko_one, 'gecko2': gecko_two, 'gecko1_morphs': gecko_one_morphs, 'gecko2_morphs': gecko_two_morphs,
              'parent_morph_set': parent_morphs, 'potential_morphs': all_potential_morphs, 'all_morphs': all_morphs_pass_two}
    return render(request, 'gecko_partial.html', context)

# Tools
def find_morphs_requiring_morph(req_morph):
    combo_morphs = gecko_M.Morph_Combo.objects.all()
    print(combo_morphs)
    applicable_morphs = set(())
    for morph in combo_morphs:
        #print(f"Checking for required morph:{req_morph} in {morph}")
        #print(f"Comparing {morph.first_req_morph} with {req_morph}")
        if morph.first_req_morph == req_morph:
            print("Morph 1 match, ADDING: " + str(morph))
            applicable_morphs.add(morph)
        elif morph.second_req_morph == req_morph:
            print("Morph 2 match")
            applicable_morphs.add(morph)
        elif morph.third_req_morph == req_morph:
            print("Morph 3 match")
            applicable_morphs.add(morph)
        elif morph.fourth_req_morph == req_morph:
            print("Morph 4 match")
            applicable_morphs.add(morph)
        elif morph.fifth_req_morph == req_morph:
            applicable_morphs.add(morph)
        elif morph.sixth_req_morph == req_morph:
            applicable_morphs.add(morph)
        elif morph.seventh_req_morph == req_morph:
            applicable_morphs.add(morph)
        elif morph.eighth_req_morph == req_morph:
            applicable_morphs.add(morph)
        elif morph.ninth_req_morph == req_morph:
            applicable_morphs.add(morph)
        elif morph.tenth_req_morph == req_morph:
            applicable_morphs.add(morph)

    print("!!!!!!!!!!!!!!!!!!!!==================!!!!!!!!!!!!!!!!!!!!!!!!!")
    print("Applicable Morphs: ", applicable_morphs)
    return applicable_morphs
    

def construct_morph_set(gecko_one_morphs, gecko_two_morphs):
    #Construct a Set (No duplicates) of morphs.
    morph_set = set(())
    for morph in gecko_one_morphs:
        morph_set.add(morph)
    for morph in gecko_two_morphs:
        morph_set.add(morph)
    return morph_set


def find_potential_morphs(parent_morphs):
    potential_morphs = set(())
    for morph in parent_morphs:
        for applicable_morph in find_morphs_requiring_morph(morph):
            potential_morphs.add(check_if_all_morphs(applicable_morph, parent_morphs))

    print("Morphs that passed: ", potential_morphs)
    return potential_morphs

def check_if_all_morphs(potential_morph, parent_morphs):
    # Check if all morphs present for req_morphs.
    pet_morph_dict = {
        "1": potential_morph.first_req_morph,
        "2": potential_morph.second_req_morph,
        "3": potential_morph.third_req_morph if potential_morph.third_req_morph != None else True,
        "4": potential_morph.fourth_req_morph if potential_morph.fourth_req_morph != None else True,
        "5": potential_morph.fifth_req_morph if potential_morph.fifth_req_morph != None else True,
        "6": potential_morph.sixth_req_morph if potential_morph.sixth_req_morph != None else True,
        "7": potential_morph.seventh_req_morph if potential_morph.seventh_req_morph != None else True,
        "8": potential_morph.eighth_req_morph if potential_morph.eighth_req_morph != None else True,
        "9": potential_morph.ninth_req_morph if potential_morph.ninth_req_morph != None else True,
        "10": potential_morph.tenth_req_morph if potential_morph.tenth_req_morph != None else True,
    }

    # for k in pet_morph_dict:
    #     print(f"{k}: {pet_morph_dict[k]}")

    for morph in pet_morph_dict:
        if pet_morph_dict[morph] != True:
            for parent_morph in parent_morphs:
                if pet_morph_dict[morph] == parent_morph:
                    pet_morph_dict[morph] = True

    # print("Post check.")
    # for k in pet_morph_dict:
    #     print(f"{k}: {pet_morph_dict[k]}")

    for morph in pet_morph_dict:
        if pet_morph_dict[morph] != True:
            return None
    print(potential_morph)
    return potential_morph.morph


def decon_morphs(parent_morphs):
    combo_morph_set = set(())
    decon_morphs = set(())

    for morph in parent_morphs:
        try:
            combo_morph_set.add(gecko_M.Morph_Combo.objects.filter(morph=morph).last())
        except:
            print("No morph.")
    for morph in combo_morph_set:
        try:
            decon_morphs.add(morph.first_req_morph)
            decon_morphs.add(morph.second_req_morph)
            if morph.third_req_morph:
                decon_morphs.add(morph.third_req_morph)
            if morph.fourth_req_morph:
                decon_morphs.add(morph.fourth_req_morph)
            if morph.fifth_req_morph:
                decon_morphs.add(morph.fifth_req_morph)
            if morph.sixth_req_morph:
                decon_morphs.add(morph.sixth_req_morph)
            if morph.seventh_req_morph:
                decon_morphs.add(morph.seventh_req_morph)
            if morph.eighth_req_morph:
                decon_morphs.add(morph.eighth_req_morph)
            if morph.ninth_req_morph:
                decon_morphs.add(morph.ninth_req_morph)
            if morph.tenth_req_morph:
                decon_morphs.add(morph.tenth_req_morph)
        except:
            "No further recursion available"

    return decon_morphs