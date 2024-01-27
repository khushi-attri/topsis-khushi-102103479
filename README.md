# topsis-khushi-102103479
submitted by: Khushi attri Roll no: 102103479 Group: 3COE17

topsis-khushi-102103479 is a Python library for dealing with Multiple Criteria Decision Making(MCDM) problems by using Technique for Order of Preference by Similarity to Ideal Solution(TOPSIS).

## Installation
Use the package manager pip to install topsis-khushi-102103479.

```pip install topsis-khushi-102103479```

## Usage
Enter csv filename followed by .csv extentsion, then enter the weights vector with vector values separated by commas, followed by the impacts vector with comma separated signs (+,-)

```topsis sample.csv "1,1,1,1" "+,-,+,+"```

## Example
### sample.csv
A csv file showing data for different mobile handsets having varying features.

| Model | Storage space (in GB) | Camera (in MP) | Price (in $) | Looks (out of 5) |
|-------|------------------------|-----------------|--------------|------------------|
| M1    | 16                     | 12              | 250          | 5                |
| M2    | 16                     | 8               | 200          | 3                |
| M3    | 32                     | 16              | 300          | 4                |
| M4    | 32                     | 8               | 275          | 4                |
| M5    | 16                     | 16              | 225          | 2                |

weights vector = [ 0.25 , 0.25 , 0.25 , 0.25 ]

impacts vector = [ + , + , - , + ]

## input:
```topsis sample.csv "0.25,0.25,0.25,0.25" "+,+,-,+"```

## output:

      TOPSIS RESULTS
-----------------------------

    P-Score  Rank
1  0.534277     3
2  0.308368     5
3  0.691632     1
4  0.534737     2
5  0.401046     4

## License
2024 Khushi Attri