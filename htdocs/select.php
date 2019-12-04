<?php
header("Cache-Control: no-store, no-cache, must-revalidate, max-age=0");
header("Cache-Control: post-check=0, pre-check=0", false);
header("Pragma: no-cache");
?>
<?php
include("config.php");
$timestamp_start=$_GET['start'];
$timestamp_end=$_GET['end'];


$sql="SELECT `id`, `timestamp_start`, `open`, `close`, `min`, `max` FROM `idicator5m` WHERE `timestamp_start`>=$timestamp_start AND `timestamp_start`<=$timestamp_end"; //tinh ca start va end
//echo $sql;
$result = $conn->query($sql);
if ($result->num_rows > 0) {
    // output data of each row
    while($row = $result->fetch_assoc()) {
    	echo $row["timestamp_start"].'|'.$row["open"].'|'.$row["close"].'|'.$row["min"].'|'.$row["max"]."<br>";
    }
} else {
    echo "0 results";
}
$conn->close();
?>