

```python
import pandas as pd
import numpy as np

```


```python
import json
with open("/Users/arjun.maniyar/Documents/Project Files/GWAR201802DATA4-Class-Repository-DATA/02-Homework/04-Numpy-Pandas/Instructions/HeroesOfPymoli/purchase_data.json") as datafile:
    data = json.load(datafile)
dataframe = pd.DataFrame(data)
dataframe.head()
```




<div>
<style scoped>
    .dataframe tbody tr th:only-of-type {
        vertical-align: middle;
    }

    .dataframe tbody tr th {
        vertical-align: top;
    }

    .dataframe thead th {
        text-align: right;
    }
</style>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>Age</th>
      <th>Gender</th>
      <th>Item ID</th>
      <th>Item Name</th>
      <th>Price</th>
      <th>SN</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>0</th>
      <td>38</td>
      <td>Male</td>
      <td>165</td>
      <td>Bone Crushing Silver Skewer</td>
      <td>3.37</td>
      <td>Aelalis34</td>
    </tr>
    <tr>
      <th>1</th>
      <td>21</td>
      <td>Male</td>
      <td>119</td>
      <td>Stormbringer, Dark Blade of Ending Misery</td>
      <td>2.32</td>
      <td>Eolo46</td>
    </tr>
    <tr>
      <th>2</th>
      <td>34</td>
      <td>Male</td>
      <td>174</td>
      <td>Primitive Blade</td>
      <td>2.46</td>
      <td>Assastnya25</td>
    </tr>
    <tr>
      <th>3</th>
      <td>21</td>
      <td>Male</td>
      <td>92</td>
      <td>Final Critic</td>
      <td>1.36</td>
      <td>Pheusrical25</td>
    </tr>
    <tr>
      <th>4</th>
      <td>23</td>
      <td>Male</td>
      <td>63</td>
      <td>Stormfury Mace</td>
      <td>1.27</td>
      <td>Aela59</td>
    </tr>
  </tbody>
</table>
</div>




```python
# counting the number of places
num_players = dataframe["SN"].nunique()
count_num = pd.DataFrame ({"Total Players": [num_players]})
count_num
```




<div>
<style scoped>
    .dataframe tbody tr th:only-of-type {
        vertical-align: middle;
    }

    .dataframe tbody tr th {
        vertical-align: top;
    }

    .dataframe thead th {
        text-align: right;
    }
</style>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>Total Players</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>0</th>
      <td>573</td>
    </tr>
  </tbody>
</table>
</div>




```python
# Unique items
unique_items = dataframe["Item Name"].nunique()

# Average prices
ave_price = dataframe["Price"].mean()

# Total Number of Purchases
purchases = dataframe["SN"].count()

# Calc total revenue
total_rev = dataframe["Price"].sum()

analysis_df = pd.DataFrame({"Number of Unique Items":[unique_items],
                           "Average Price":[ave_price],
                           "Number of Purchases":[purchases],
                           "Total Revenue":[total_rev]})
# Reposition columns
analysis_reposition = analysis_df[["Number of Unique Items",
                                  "Average Price",
                                  "Number of Purchases",
                                  "Total Revenue"
                                  ]]
# Formatting Price and revenue with Map to include $ sign
analysis_reposition["Average Price"] = analysis_reposition["Average Price"].map("${:.2f}".format)
analysis_reposition["Total Revenue"] = analysis_reposition["Total Revenue"].map("${:.2f}".format)
analysis_reposition

```




<div>
<style scoped>
    .dataframe tbody tr th:only-of-type {
        vertical-align: middle;
    }

    .dataframe tbody tr th {
        vertical-align: top;
    }

    .dataframe thead th {
        text-align: right;
    }
</style>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>Number of Unique Items</th>
      <th>Average Price</th>
      <th>Number of Purchases</th>
      <th>Total Revenue</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>0</th>
      <td>179</td>
      <td>$2.93</td>
      <td>780</td>
      <td>$2286.33</td>
    </tr>
  </tbody>
</table>
</div>




```python
# Gender
gender =dataframe[["SN", "Gender"]]
gender_no_dupes = gender.drop_duplicates(["SN"])
gender_count = gender_no_dupes["Gender"].value_counts()
gender_print = pd.DataFrame({"Total Count":gender_count
                            })

percentages = (gender_print["Total Count"]/573)*100
gender_print["Percentage of Players"] = percentages
gender_print = pd.DataFrame({"Total Count":gender_count,
                            "Percentage of Players": percentages
                            })
gender_print["Percentage of Players"] = gender_print["Percentage of Players"].map("{:.2f}%".format)
gender_print

```




<div>
<style scoped>
    .dataframe tbody tr th:only-of-type {
        vertical-align: middle;
    }

    .dataframe tbody tr th {
        vertical-align: top;
    }

    .dataframe thead th {
        text-align: right;
    }
</style>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>Percentage of Players</th>
      <th>Total Count</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>Male</th>
      <td>81.15%</td>
      <td>465</td>
    </tr>
    <tr>
      <th>Female</th>
      <td>17.45%</td>
      <td>100</td>
    </tr>
    <tr>
      <th>Other / Non-Disclosed</th>
      <td>1.40%</td>
      <td>8</td>
    </tr>
  </tbody>
</table>
</div>




```python
# Gender Purchasing analysis

group_gen = dataframe.groupby(["Gender"])

# Purchase count
purchase_count_gen = group_gen["SN"].count()

# Ave price

ave_purchase_price = group_gen["Price"].mean()

# Total Purchase

total_purch = group_gen["Price"].sum()

# Normalized:

normalized = total_purch/gender_count

summarized_gen = pd.DataFrame({"Purchase Count":purchase_count_gen,
                              "Average Purchase Price":ave_purchase_price,
                              "Total Purchase Value":total_purch,
                              "Normalized Totals":normalized,
                              })
# Formatting
summarized_gen["Average Purchase Price"]= summarized_gen["Average Purchase Price"].map("${:.2f}".format)
summarized_gen["Total Purchase Value"]= summarized_gen["Total Purchase Value"].map("${:.2f}".format)
summarized_gen["Normalized Totals"]= summarized_gen["Normalized Totals"].map("${:.2f}".format)
summarized_gen
```




<div>
<style scoped>
    .dataframe tbody tr th:only-of-type {
        vertical-align: middle;
    }

    .dataframe tbody tr th {
        vertical-align: top;
    }

    .dataframe thead th {
        text-align: right;
    }
</style>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>Average Purchase Price</th>
      <th>Normalized Totals</th>
      <th>Purchase Count</th>
      <th>Total Purchase Value</th>
    </tr>
    <tr>
      <th>Gender</th>
      <th></th>
      <th></th>
      <th></th>
      <th></th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>Female</th>
      <td>$2.82</td>
      <td>$3.83</td>
      <td>136</td>
      <td>$382.91</td>
    </tr>
    <tr>
      <th>Male</th>
      <td>$2.95</td>
      <td>$4.02</td>
      <td>633</td>
      <td>$1867.68</td>
    </tr>
    <tr>
      <th>Other / Non-Disclosed</th>
      <td>$3.25</td>
      <td>$4.47</td>
      <td>11</td>
      <td>$35.74</td>
    </tr>
  </tbody>
</table>
</div>




```python
# Age Demographics
# Bins
bins = [0,10,14,19,24,29,34,39,100]
groups = ["<10", "10-14", "15-19", "20-24", "25-29", "30-34", "35-39", "40+"]
dataframe[" "] = pd.cut(dataframe["Age"], bins, labels = groups)
binned_age = dataframe.groupby (" ")

purchase_count_gen =binned_age["Age"].count()
ave_purchase_price = binned_age["Price"].mean()
total_purch = binned_age["Price"].sum()

unique_purchasers = binned_age[" "].count()

# Normalized
normalized_age = total_purch/unique_purchasers

age_df = pd.DataFrame({"Purchase Count":purchase_count_gen,
                      "Average Purchase Price": ave_purchase_price,
                      "Total Purchase Value":total_purch,
                      "Normalized Totals":normalized_age
                      })
age_df["Average Purchase Price"]= age_df["Average Purchase Price"].map("${:.2f}".format)
age_df["Total Purchase Value"]= age_df["Total Purchase Value"].map("${:.2f}".format)
age_df["Normalized Totals"]= age_df["Normalized Totals"].map("${:.2f}".format)

# Re-order columns
age_df2 = age_df[["Purchase Count",
                 "Average Purchase Price",
                 "Total Purchase Value",
                 "Normalized Totals"
                 ]]
age_df2
```




<div>
<style scoped>
    .dataframe tbody tr th:only-of-type {
        vertical-align: middle;
    }

    .dataframe tbody tr th {
        vertical-align: top;
    }

    .dataframe thead th {
        text-align: right;
    }
</style>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>Purchase Count</th>
      <th>Average Purchase Price</th>
      <th>Total Purchase Value</th>
      <th>Normalized Totals</th>
    </tr>
    <tr>
      <th></th>
      <th></th>
      <th></th>
      <th></th>
      <th></th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>&lt;10</th>
      <td>32</td>
      <td>$3.02</td>
      <td>$96.62</td>
      <td>$3.02</td>
    </tr>
    <tr>
      <th>10-14</th>
      <td>31</td>
      <td>$2.70</td>
      <td>$83.79</td>
      <td>$2.70</td>
    </tr>
    <tr>
      <th>15-19</th>
      <td>133</td>
      <td>$2.91</td>
      <td>$386.42</td>
      <td>$2.91</td>
    </tr>
    <tr>
      <th>20-24</th>
      <td>336</td>
      <td>$2.91</td>
      <td>$978.77</td>
      <td>$2.91</td>
    </tr>
    <tr>
      <th>25-29</th>
      <td>125</td>
      <td>$2.96</td>
      <td>$370.33</td>
      <td>$2.96</td>
    </tr>
    <tr>
      <th>30-34</th>
      <td>64</td>
      <td>$3.08</td>
      <td>$197.25</td>
      <td>$3.08</td>
    </tr>
    <tr>
      <th>35-39</th>
      <td>42</td>
      <td>$2.84</td>
      <td>$119.40</td>
      <td>$2.84</td>
    </tr>
    <tr>
      <th>40+</th>
      <td>17</td>
      <td>$3.16</td>
      <td>$53.75</td>
      <td>$3.16</td>
    </tr>
  </tbody>
</table>
</div>




```python
# Big Spenders
top_spender = dataframe.groupby(["SN"])

pur_cnt = top_spender["SN"].count()

ave_purchase_price = top_spender["Price"].mean()

total_purch = top_spender["Price"].sum()

# Summarize
sum_top_spender = pd.DataFrame({"Purchase Count":pur_cnt,
                               "Average Purchase Price":ave_purchase_price,
                               "Total Purchase Value": total_purch
                               })


# Column adjustment
sum_top_spender2 = sum_top_spender[["Purchase Count",
                                   "Average Purchase Price",
                                   "Total Purchase Value"]]
sum_top_spender3 = sum_top_spender2.sort_values("Total Purchase Value", ascending = False)
# Making it look pretty
sum_top_spender3["Average Purchase Price"] = sum_top_spender3["Average Purchase Price"].map("${:.2f}".format)
sum_top_spender3["Total Purchase Value"] = sum_top_spender3["Total Purchase Value"].map("${:.2f}".format)
sum_top_spender3.head()


```




<div>
<style scoped>
    .dataframe tbody tr th:only-of-type {
        vertical-align: middle;
    }

    .dataframe tbody tr th {
        vertical-align: top;
    }

    .dataframe thead th {
        text-align: right;
    }
</style>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>Purchase Count</th>
      <th>Average Purchase Price</th>
      <th>Total Purchase Value</th>
    </tr>
    <tr>
      <th>SN</th>
      <th></th>
      <th></th>
      <th></th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>Undirrala66</th>
      <td>5</td>
      <td>$3.41</td>
      <td>$17.06</td>
    </tr>
    <tr>
      <th>Saedue76</th>
      <td>4</td>
      <td>$3.39</td>
      <td>$13.56</td>
    </tr>
    <tr>
      <th>Mindimnya67</th>
      <td>4</td>
      <td>$3.18</td>
      <td>$12.74</td>
    </tr>
    <tr>
      <th>Haellysu29</th>
      <td>3</td>
      <td>$4.24</td>
      <td>$12.73</td>
    </tr>
    <tr>
      <th>Eoda93</th>
      <td>3</td>
      <td>$3.86</td>
      <td>$11.58</td>
    </tr>
  </tbody>
</table>
</div>




```python
# Most Popular Items
pop_items = dataframe.groupby(["Item ID", "Item Name"])

pur_cnt = pop_items["SN"].count()

ave_purchase_price= pop_items["Price"].mean()

total_purch = pop_items["Price"].sum()

sum_pop_items = pd.DataFrame({"Purchase Count":pur_cnt,
                             "Item Price": ave_purchase_price,
                             "Total Purchase Value":total_purch
                             })
sum_pop_items2 = sum_pop_items[["Purchase Count",
                                       "Item Price",
                                       "Total Purchase Value",
                                       ]]
sum_pop_items3 = sum_pop_items2.sort_values('Purchase Count', ascending=False)
sum_pop_items3["Item Price"] = sum_pop_items3["Item Price"].map("${:.2f}".format)
sum_pop_items3["Total Purchase Value"] = sum_pop_items3["Total Purchase Value"].map("${:.2f}".format)
sum_pop_items3.head()


```




<div>
<style scoped>
    .dataframe tbody tr th:only-of-type {
        vertical-align: middle;
    }

    .dataframe tbody tr th {
        vertical-align: top;
    }

    .dataframe thead th {
        text-align: right;
    }
</style>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th></th>
      <th>Purchase Count</th>
      <th>Item Price</th>
      <th>Total Purchase Value</th>
    </tr>
    <tr>
      <th>Item ID</th>
      <th>Item Name</th>
      <th></th>
      <th></th>
      <th></th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>39</th>
      <th>Betrayal, Whisper of Grieving Widows</th>
      <td>11</td>
      <td>$2.35</td>
      <td>$25.85</td>
    </tr>
    <tr>
      <th>84</th>
      <th>Arcane Gem</th>
      <td>11</td>
      <td>$2.23</td>
      <td>$24.53</td>
    </tr>
    <tr>
      <th>31</th>
      <th>Trickster</th>
      <td>9</td>
      <td>$2.07</td>
      <td>$18.63</td>
    </tr>
    <tr>
      <th>175</th>
      <th>Woeful Adamantite Claymore</th>
      <td>9</td>
      <td>$1.24</td>
      <td>$11.16</td>
    </tr>
    <tr>
      <th>13</th>
      <th>Serenity</th>
      <td>9</td>
      <td>$1.49</td>
      <td>$13.41</td>
    </tr>
  </tbody>
</table>
</div>




```python
# Most Profitable Items
prof_items = dataframe.groupby(["Item ID"])

pur_cnt = prof_items["SN"].count()

ave_purchase_price= prof_items["Price"].mean()

total_purch = prof_items["Price"].sum()

sum_prof_items = pd.DataFrame({"Purchase Count":pur_cnt,
                             "Item Price": ave_purchase_price,
                             "Total Purchase Value":total_purch
                             })
sum_prof_items2 = sum_prof_items[["Purchase Count",
                                       "Item Price",
                                       "Total Purchase Value",
                                       ]]
sum_prof_items3 = sum_prof_items2.sort_values('Total Purchase Value', ascending=False)
sum_prof_items3["Item Price"] = sum_prof_items3["Item Price"].map("${:.2f}".format)
sum_prof_items3["Total Purchase Value"] = sum_prof_items3["Total Purchase Value"].map("${:.2f}".format)
sum_prof_items3.head()
```




<div>
<style scoped>
    .dataframe tbody tr th:only-of-type {
        vertical-align: middle;
    }

    .dataframe tbody tr th {
        vertical-align: top;
    }

    .dataframe thead th {
        text-align: right;
    }
</style>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>Purchase Count</th>
      <th>Item Price</th>
      <th>Total Purchase Value</th>
    </tr>
    <tr>
      <th>Item ID</th>
      <th></th>
      <th></th>
      <th></th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>34</th>
      <td>9</td>
      <td>$4.14</td>
      <td>$37.26</td>
    </tr>
    <tr>
      <th>115</th>
      <td>7</td>
      <td>$4.25</td>
      <td>$29.75</td>
    </tr>
    <tr>
      <th>32</th>
      <td>6</td>
      <td>$4.95</td>
      <td>$29.70</td>
    </tr>
    <tr>
      <th>103</th>
      <td>6</td>
      <td>$4.87</td>
      <td>$29.22</td>
    </tr>
    <tr>
      <th>107</th>
      <td>8</td>
      <td>$3.61</td>
      <td>$28.88</td>
    </tr>
  </tbody>
</table>
</div>


