# Generate Map From Image

* First of all, make sure you clone the repository with the following command:

```bash
$> git clone git@github.com:ArthurSobreira/map_generator.git
```

* Then, you need to install the <strong>Pillow</strong> and <strong>Numpy</strong> packages, with the following commands:

```bash
$> pip install Pillow
$> pip install numpy
```

* Now, to create properly formatted maps that can be read by <strong>Fdf</strong>, simply have access to an image (PNG or JPG)
  and run the script <code>map_generator.py</code> with the following command:

```bash
$> python3 map_generator.py
$>
$> Enter the image path: <image-name>
$> Enter the name that the image will be saved: <map-name>.fdf
```

* Once the map is generated, to render it just execute the command seen previously, with this it is possible to generate some really cool maps, like these:

<br>

<div align="center">
  <a href="images/van-gogh.png" target="_blank">
      <img height=550 src="images/van-gogh.png">
   </a>
</div><br>
<div align="center">
   <a href="images/got_map.png" target="_blank">
      <img height=550 src="images/got_map.png">
   </a>
</div><br>
<div align="center">
   <a href="images/monalisa.png" target="_blank">
      <img height=550 src="images/monalisa.png">
   </a>
</div><br>
