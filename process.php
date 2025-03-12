<?php
    $a = escapeshellarg($_POST["a"]);
    $b = escapeshellarg($_POST["b"]);
    
    $command = "python3 bitwise_operations.py $a $b";
    $output = shell_exec($command);
    
    echo "<div>$output</div>";
?>