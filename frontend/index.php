<html>
	<body>

		<h1>Products</h1>
                <ul>
		<?php
			$json = file_get_contents('http://15.206.194.24:8080');
                        $obj = json_decode($json);
                        $products = $obj->products;
                        foreach ($products as $item) {
                          echo "<li>$item</li>";
                      }
		?>
                </ul>

	</body>
</html>
