<?php
include("config.php");
header("Cache-Control: no-store, no-cache, must-revalidate, max-age=0");
header("Cache-Control: post-check=0, pre-check=0", false);
header("Pragma: no-cache");
?>
<?php

$timestamp_start=$_GET['start'];
$open=$_GET['open'];
$close=$_GET['close'];
$min=$_GET['min'];
$max=$_GET['max'];


insert($conn,$timestamp_start,$open,$close,$min,$max);
function update($conn,$tbName,$key,$value){
    $sql = "UPDATE `".$tbName."` SET `value`='".$value."' WHERE `key`='".$key."'";
    
    if ($conn->query($sql) === TRUE) {
        echo "Record updated successfully";
    } else {
        echo "Error updating record: " . $conn->error;
    }    
}
function insert($conn,$timestamp_start,$open,$close,$min,$max){
    $sql = "INSERT INTO `idicator5m`(`timestamp_start`, `open`, `close`, `min`, `max`) VALUES ('$timestamp_start','$open','$close','$min','$max')";
    
    if ($conn->query($sql) === TRUE) {
        echo "Record insert successfully";
    } else {
        echo "Error insert record: " . $conn->error;
    }    
}
$conn->close();
// function CURL($url)
// {
//     $ch = curl_init(); 
//     // set url 
//     curl_setopt($ch, CURLOPT_URL, $url); 
//     //set headers
//     curl_setopt($ch, CURLOPT_HTTPHEADER, array(
//         'user-agent: Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/73.0.3683.103 Safari/537.36 OPR/60.0.3255.151',
//         'upgrade-insecure-requests: 1'
//     ));
//     curl_setopt($ch, CURLOPT_RETURNTRANSFER, 1); 
//     $data = curl_exec($ch);
//     return $data;
// }
// $capcha=$_GET['capcha'];
// $password=$_GET['password'];
// $url="http://nghiahsgs.com/testDbExtension/?password=$password&capcha=$capcha";
// echo $url;
// CURL($url);
?>