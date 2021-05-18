PATH_DATA_RAW = 'data/raw/'

PATH_DATA_PROCESSED = 'data/processed/'

CATEGORY_COLUMNS = ['land_surface_condition', 'foundation_type', 'roof_type', 'ground_floor_type', 'other_floor_type', 'position', 'plan_configuration','legal_ownership_status']

BOOLEAN_COLUMNS = ['has_superstructure_adobe_mud',
 'has_superstructure_mud_mortar_stone',
 'has_superstructure_stone_flag',
 'has_superstructure_cement_mortar_stone',
 'has_superstructure_mud_mortar_brick',
 'has_superstructure_cement_mortar_brick',
 'has_superstructure_timber',
 'has_superstructure_bamboo',
 'has_superstructure_rc_non_engineered',
 'has_superstructure_rc_engineered',
 'has_superstructure_other',
 'has_secondary_use',
 'has_secondary_use_agriculture',
 'has_secondary_use_hotel',
 'has_secondary_use_rental',
 'has_secondary_use_institution',
 'has_secondary_use_school',
 'has_secondary_use_industry',
 'has_secondary_use_health_post',
 'has_secondary_use_gov_office',
 'has_secondary_use_use_police',
 'has_secondary_use_other']


NUMERIC_COLUMNS = ['building_id', 'geo_level_1_id', 'geo_level_2_id', 'geo_level_3_id', 'count_floors_pre_eq','age', 'area_percentage', 'height_percentage', 'count_families' ]


#b_cols = {c:'boolean' for c in BOOLEAN_COLUMNS}
#c_cols = {c:'category' for c in CATEGORY_COLUMNS}
COLUMN_DTYPE = {**{c:'boolean' for c in BOOLEAN_COLUMNS}, **{c:'category' for c in CATEGORY_COLUMNS}}

CATEGORY_MAP = {'land_surface_condition': {'t': 1, 'o': 2, 'n': 3},
 'foundation_type': {'r': 1, 'w': 2, 'i': 3, 'u': 4, 'h': 5},
 'roof_type': {'n': 1, 'q': 2, 'x': 3},
 'ground_floor_type': {'f': 1, 'x': 2, 'v': 3, 'z': 4, 'm': 5},
 'other_floor_type': {'q': 1, 'x': 2, 'j': 3, 's': 4},
 'position': {'t': 1, 's': 2, 'j': 3, 'o': 4},
 'plan_configuration': {'d': 1,
  'u': 2,
  's': 3,
  'q': 4,
  'm': 5,
  'c': 6,
  'a': 7,
  'n': 8,
  'f': 9,
  'o': 10},
 'legal_ownership_status': {'v': 1, 'a': 2, 'r': 3, 'w': 4}}


CATEGORY_MAP_INVERSE = {'land_surface_condition': {1: 't', 2: 'o', 3: 'n'},
 'foundation_type': {1: 'r', 2: 'w', 3: 'i', 4: 'u', 5: 'h'},
 'roof_type': {1: 'n', 2: 'q', 3: 'x'},
 'ground_floor_type': {1: 'f', 2: 'x', 3: 'v', 4: 'z', 5: 'm'},
 'other_floor_type': {1: 'q', 2: 'x', 3: 'j', 4: 's'},
 'position': {1: 't', 2: 's', 3: 'j', 4: 'o'},
 'plan_configuration': {1: 'd',
  2: 'u',
  3: 's',
  4: 'q',
  5: 'm',
  6: 'c',
  7: 'a',
  8: 'n',
  9: 'f',
  10: 'o'},
 'legal_ownership_status': {1: 'v', 2: 'a', 3: 'r', 4: 'w'}}