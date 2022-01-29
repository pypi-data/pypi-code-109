"""Auto-generated file, do not edit by hand. AU metadata"""
from ..phonemetadata import NumberFormat, PhoneNumberDesc, PhoneMetadata

PHONE_METADATA_AU = PhoneMetadata(id='AU', country_code=61, international_prefix='001[14-689]|14(?:1[14]|34|4[17]|[56]6|7[47]|88)0011',
    general_desc=PhoneNumberDesc(national_number_pattern='1(?:[0-79]\\d{7}(?:\\d(?:\\d{2})?)?|8[0-24-9]\\d{7})|[2-478]\\d{8}|1\\d{4,7}', possible_length=(5, 6, 7, 8, 9, 10, 12)),
    fixed_line=PhoneNumberDesc(national_number_pattern='(?:(?:2(?:[0-26-9]\\d|3[0-8]|4[02-9]|5[0135-9])|3(?:[0-3589]\\d|4[0-578]|6[1-9]|7[0-35-9])|7(?:[013-57-9]\\d|2[0-8]))\\d{3}|8(?:51(?:0(?:0[03-9]|[12479]\\d|3[2-9]|5[0-8]|6[1-9]|8[0-7])|1(?:[0235689]\\d|1[0-69]|4[0-589]|7[0-47-9])|2(?:0[0-79]|[18][13579]|2[14-9]|3[0-46-9]|[4-6]\\d|7[89]|9[0-4]))|(?:6[0-8]|[78]\\d)\\d{3}|9(?:[02-9]\\d{3}|1(?:(?:[0-58]\\d|6[0135-9])\\d|7(?:0[0-24-9]|[1-9]\\d)|9(?:[0-46-9]\\d|5[0-79])))))\\d{3}', example_number='212345678', possible_length=(9,), possible_length_local_only=(8,)),
    mobile=PhoneNumberDesc(national_number_pattern='4(?:83[0-38]|93[0-6])\\d{5}|4(?:[0-3]\\d|4[047-9]|5[0-25-9]|6[06-9]|7[02-9]|8[0-24-9]|9[0-27-9])\\d{6}', example_number='412345678', possible_length=(9,)),
    toll_free=PhoneNumberDesc(national_number_pattern='180(?:0\\d{3}|2)\\d{3}', example_number='1800123456', possible_length=(7, 10)),
    premium_rate=PhoneNumberDesc(national_number_pattern='190[0-26]\\d{6}', example_number='1900123456', possible_length=(10,)),
    shared_cost=PhoneNumberDesc(national_number_pattern='13(?:00\\d{6}(?:\\d{2})?|45[0-4]\\d{3})|13\\d{4}', example_number='1300123456', possible_length=(6, 8, 10, 12)),
    voip=PhoneNumberDesc(national_number_pattern='14(?:5(?:1[0458]|[23][458])|71\\d)\\d{4}', example_number='147101234', possible_length=(9,)),
    pager=PhoneNumberDesc(national_number_pattern='163\\d{2,6}', example_number='1631234', possible_length=(5, 6, 7, 8, 9)),
    no_international_dialling=PhoneNumberDesc(national_number_pattern='1(?:3(?:00\\d{5}|45[0-4])|802)\\d{3}|1[38]00\\d{6}|13\\d{4}', possible_length=(6, 7, 8, 10, 12)),
    preferred_international_prefix='0011',
    national_prefix='0',
    national_prefix_for_parsing='0|(183[12])',
    number_format=[NumberFormat(pattern='(\\d{2})(\\d{3,4})', format='\\1 \\2', leading_digits_pattern=['16'], national_prefix_formatting_rule='0\\1'),
        NumberFormat(pattern='(\\d{2})(\\d{2})(\\d{2})', format='\\1 \\2 \\3', leading_digits_pattern=['13']),
        NumberFormat(pattern='(\\d{3})(\\d{3})', format='\\1 \\2', leading_digits_pattern=['19']),
        NumberFormat(pattern='(\\d{3})(\\d{4})', format='\\1 \\2', leading_digits_pattern=['180', '1802']),
        NumberFormat(pattern='(\\d{4})(\\d{3,4})', format='\\1 \\2', leading_digits_pattern=['19']),
        NumberFormat(pattern='(\\d{2})(\\d{3})(\\d{2,4})', format='\\1 \\2 \\3', leading_digits_pattern=['16'], national_prefix_formatting_rule='0\\1'),
        NumberFormat(pattern='(\\d{3})(\\d{3})(\\d{3})', format='\\1 \\2 \\3', leading_digits_pattern=['14|4'], national_prefix_formatting_rule='0\\1'),
        NumberFormat(pattern='(\\d)(\\d{4})(\\d{4})', format='\\1 \\2 \\3', leading_digits_pattern=['[2378]'], national_prefix_formatting_rule='(0\\1)', domestic_carrier_code_formatting_rule='$CC (\\1)'),
        NumberFormat(pattern='(\\d{4})(\\d{3})(\\d{3})', format='\\1 \\2 \\3', leading_digits_pattern=['1(?:30|[89])']),
        NumberFormat(pattern='(\\d{4})(\\d{4})(\\d{4})', format='\\1 \\2 \\3', leading_digits_pattern=['130'])],
    intl_number_format=[NumberFormat(pattern='(\\d{2})(\\d{3,4})', format='\\1 \\2', leading_digits_pattern=['16']),
        NumberFormat(pattern='(\\d{2})(\\d{3})(\\d{2,4})', format='\\1 \\2 \\3', leading_digits_pattern=['16']),
        NumberFormat(pattern='(\\d{3})(\\d{3})(\\d{3})', format='\\1 \\2 \\3', leading_digits_pattern=['14|4']),
        NumberFormat(pattern='(\\d)(\\d{4})(\\d{4})', format='\\1 \\2 \\3', leading_digits_pattern=['[2378]']),
        NumberFormat(pattern='(\\d{4})(\\d{3})(\\d{3})', format='\\1 \\2 \\3', leading_digits_pattern=['1(?:30|[89])'])],
    main_country_for_code=True,
    mobile_number_portable_region=True)
