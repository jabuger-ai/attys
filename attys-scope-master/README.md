# attys-scope (Linux / Windows)

![alt tag](attys_emg_measurement.jpg)

## Data format

For saving data to a file the format is either "comma separated" (CSV) or "tab separated" (TSV).

UDP packets are always transmitted as CSV.


### Header

```
# TIMESTAMP_IN_UNIX_EPOCH ATTYS1MAC ATTYS2MAC ...
```

### Columns

0. TIME
1. RAW_AccX
2. RAW_AccY
3. RAW_AccZ
4. RAW_MagX
5. RAW_MagY
6. RAW_MagZ
7. RAW_CH1
8. RAW_CH2
9. RAW_DIO1
10. RAW_DIO2 
11. FILT_1
12. FILT_2
13. FILT_3
14. FILT_4
15. FILT_5
16. FILT_6
17. FILT_7
18. FILT_8
19. FILT_9
20. FILT_10
21. RAW_AccX of the 2nd Attys
22. ...


## Windows installer

[is here](installer/attys_scope_installer.msi)

## Ubuntu packages for Ubuntu LTS releases
Add these two repositories...
```
sudo add-apt-repository ppa:berndporr/attys
sudo add-apt-repository ppa:berndporr/dsp
```
...and then select attys-scope. This will then install also
the other required packages.
