<html>
    <head>
        <title>ETL container</title>
    </head>

    <body>
        <h1>ETL container</h1>
        <h2>Created by Jordi Rodeiro</h2>
            <?php
                $content = file_get_contents('http://etl_app/');

                $rows = preg_split('/\s+/', $content);

                foreach($rows as  $row) {
                    if (str_contains($row, "&")) {
                        echo "<br>";
                        echo "<ul style='font-size:40px'> <b>";
                        echo explode('&', $row)[0];
                        echo "</b>";
                    } else {
                        echo "<ul>";
                        $replace1 = str_replace(',', ': ', $row);
                        echo str_replace('_', ' ', $replace1);
                    }
                    echo "</ul>";
                }
            ?>

    </body>
</html>
