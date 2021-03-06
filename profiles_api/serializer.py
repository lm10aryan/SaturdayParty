from rest_framework import serializers
from .models import UserProfile
from djoser.serializers import UserCreateSerializer,UserSerializer
from profiles_api.models import farmer,fields_info,products_info,CropNames,QuestionSheet,PhaseDecider,PhaseQuestionLinker,DailyAlertCycle

class UserCreateSerializer(UserCreateSerializer):
    class Meta(UserCreateSerializer.Meta):
        model = UserProfile
        fields=('id','phone_number','password')



class FarmerSerializer(serializers.ModelSerializer):
    class Meta:
        model=farmer
        fields=[
            'farmer_id',
            'f_name',
            'l_name',
            'street',
            'village',
            'district',
            'state',
            'pin_code',
        ]


class FieldSerializer(serializers.ModelSerializer):
    class Meta:
        model=fields_info
        fields=[
            'field_id',
            'farmer',
            'street',
            'village',
            'district',
            'state',
            'pin_code',
            'total_acres',
        ]

class ProductsInfoSerializer(serializers.ModelSerializer):
    class Meta:
        model=products_info
        fields=[
            'product_id',
            'field',
            'product_name',
            'date_of_start',
            'seed_type',
            'acres',
        ]
class CropNamesSerializer(serializers.ModelSerializer):
    class Meta:
        model=CropNames
        fields=[
            'crop_id',
            'crop_name',
        ]

class FarmerIdSerializer(serializers.ModelSerializer):
    class Meta:
        model=farmer
        fields=[
            'farmer_id',
        ]
class FieldIdSerializer(serializers.ModelSerializer):
    class Meta:
        model=fields_info
        fields=[
            'field_id',
        ]

class QuestionSheetSerializer(serializers.ModelSerializer):
    class Meta:
        model=QuestionSheet
        fields=[
            'id',
            'past_question',
            'future_question',
            'type',
            'constraint',
            'options_text',
            'options_value',
            'question_tag',
            'past_condition',
            'future_condition',
        ]


class PhaseDeciderSerializer(serializers.ModelSerializer):
    class Meta:
        model=PhaseDecider
        fields=[
            'id',
            'crop',
            'phase_id',
            'start_day',
            'end_day',
        ]

class PhaseIdSerializer(serializers.ModelSerializer):
    class Meta:
        model=PhaseDecider
        fields=[
            'phase_id'
        ]


class PhaseQuestionLinkerSerializer(serializers.ModelSerializer):
    class Meta:
        model=PhaseQuestionLinker
        fields=[
            'phase',
            'question_id',
            'tense',
        ]

class DailyAlertCycleSerializer(serializers.ModelSerializer):
    class Meta:
        model=DailyAlertCycle
        fields=[
            'day_cycle',
            'day_action',
            'day_adv',
            'fertiliser',
            'fert_spray',
            'fert_adv',
            'diseases',
            'symptoms',
            'causes',
            'prevention'
        ]
