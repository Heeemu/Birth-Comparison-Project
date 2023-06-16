<!DOCTYPE html>
<html>
<head>
  <title>Database of Three Cities</title>
  <style>
    table {
      border-collapse: collapse;
      width: 100%;
    }
    
    th, td {
      border: 1px solid #ddd;
      padding: 8px;
      text-align: left;
    }
    
    th {
      background-color: #f2f2f2;
    }
  </style>
</head>
<body>
  <h1>User Database Viewer</h1>
  
  <table>
    <tr>
      <th>Age</th>
      <th>BirthYear</th>
      <th>City</th>
    </tr>
    
	<?php
	$host = "localhost";      // Hostname (e.g., localhost or 127.0.0.1)
	$username = "root";  // Database username
	$password = "root";  // Database password
	$database = "database";  // Database name

	// Create a connection
	$connection = mysqli_connect($host, $username, $password, $database);

	// Check the connection
	if (!$connection) {
		die("Connection failed: " . mysqli_connect_error());
	}

      
      $query = "SELECT age, birthyear, city FROM users";
      $result = mysqli_query($connection, $query);
      
      // Loop through the rows and generate table rows
      while ($row = mysqli_fetch_assoc($result)) {
        echo "<tr>";
        echo "<td>" . $row['age'] . "</td>";
        echo "<td>" . $row['birthyear'] . "</td>";
        echo "<td>" . $row['city'] . "</td>";
        echo "</tr>";
      }
      

      mysqli_close($connection);
    ?>
    
  </table>
</body>
</html>
