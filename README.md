# Lithuanian agriculture analysis 2020
 In this project I will be analyzing open data about Lithuanian agriculture

## Sources
In this project I have used data provided by VDA. Data was anonymized and cleaned before becoming open source. 
Here You can find original dataset: https://open-data-ls-osp-sdg.hub.arcgis.com/datasets/74423d36843c41c5a4fbbc110c2139cd_0/about

### Rounding Rules

- **Farm Land**: Rounded to the nearest whole number.  
- **Number of Animals**: Rounded to the nearest multiple of five (i.e., 0, 5, 10, 15, 20, ...).  
- **Standard Production**: Rounded based on the size of standard production:  
  - **[0, 100]** – rounded to the nearest 5  
  - **(100, 1000]** – rounded to the nearest 100  
  - **(1000, 10000]** – rounded to the nearest 500  
  - **(10000, ∞)** – rounded to the nearest 1000  
- **Livestock Units**: Rounded to the nearest whole number.  

### Exceptions

- **Rows 100, 101, 111, 112, and 116**:  
  If 500 hectares or more, reported as an interval – `≥500 ha`  

- **Row 2008 (Pigs)**:  
  If 100 or more, reported as an interval – `≥100`  

- **Row 2012 (Sheep)**:  
  If 100 or more, reported as an interval – `≥100`  

- **Row 2015 (Goats)**:  
  If 30 or more, reported as an interval – `≥30`  

- **Row 2019 (Poultry)**:  
  If 500 or more, reported as an interval – `≥500`  

- **Row 2029 (Rabbits)**:  
  If 100 or more, reported as an interval – `≥100`  

- **Row 2030 (Bees)**:  
  If 100 or more, reported as an interval – `≥100`  

### Coordinate System

- **LKS-94**  

### Legend

| Feature in dataset  | Meaning | Details |
| ------------- | ------------- | ------------- |
| U_VLD_LYTIS  | Gender of the owner  | 1 - male, 2- female |
| U_EKO  | Ecological farm  | 1- yes, 2 - no|
| UKININKAVIMO_KRYPTIS  | Type of farm  | More details bellow|
| EKONOMINIO_DYDZIO_KLASE  | economical size class  | More details bellow|
| STANDARTINE_PRODUKCIJA_K  | Production  | |
| SAL_GYV_K | livestock units | standardized unit for comparing different types of livestock |
| F_100_K | arable land | |
| F_101_K | pastures and meadows | |
| F_104_K | pome fruits | |
| F_105_K | stone fruits | |
| F_106_K | berry plantations | |
| F_107_K | nut trees | |
| F_108_K | tree nurseries | |
| F_109_K | other perennial plants for human consumption | weaving, wickerwork, energy purposes, short-rotation coppice in agricultural land, etc. |
| F_111_K | utilized agricultural land | |
| F_112_K | unused agricultural land | |
| F_113_K | forested areas | |
| F_115_K | other land | water bodies, land under buildings, roads, shrubs, wetlands, and other non-agricultural land | 
| F_116_K | total land area | |
| F_1037_K | greenhouses | |
| F_2000_K | total cattle | |
| F_2008_K | pigs | |
| F_2012_K | total sheep | |
| F_2015_K | total goats | |
| F_2018_K | total horses | |
| F_2019_K | poultry | |
| F_2029_K | rabbits | |
| F_2031_K | bee colonies | |

#### UKININKAVIMO_KRYPTIS

There are 8 types of farming in this dataset:

1. Field crop farming
2. Vegetable growing
3. Perennial plant growing
4. Grazing livestock farming
5. Grain-fed livestock farming
6. Mixed crop farming
7. Mixed livestock farming
8. Mixed crop and livestock farming
9. Unclassified farms

#### EKONOMINIO_DYDZIO_KLASE

There are 14 classes in this dataset:

1. < 2,000 EUR
2. 2,000–< 4,000 EUR
3. 4,000–< 8,000 EUR
4. 8,000–< 15,000 EUR
5. 15,000–< 25,000 EUR
6. 25,000–< 50,000 EUR
7. 50,000–< 100,000 EUR
8. 100,000–< 250,000 EUR
9. 250,000–< 500,000 EUR
10. 500,000–< 750,000 EUR
11. 750,000–< 1,000,000 EUR
12. 1,000,000–< 1,500,000 EUR
13. 1,500,000–< 3,000,000 EUR
14. ≥ 3,000,000 EUR

