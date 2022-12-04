<html>
    <head>
        <title>My Obsertory</title>
    </head>

    <body>
        <h1>Welcome to my observatory</h1>
            <?php
                $content = file_get_contents('http://etl_app/');
                #header('Content-Type: image/png');
                #echo $content;

                #$rows = explode(' ', $content);
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

                #echo file_get_contents('http://etl_app/');
                #$json = file_get_contents('http://etl_app/');
                #echo '<img src="{{ $json }}" alt="User Image">';
            ?>
            <?php
                #$url = "http://etl_app/";
                #$curl = curl_init();
                #curl_setopt($curl, CURLOPT_URL, $url);
                #curl_setopt($curl, CURLOPT_RETURNTRANSFER, true);
                #$picture = json_decode(curl_exec($curl), true);
                #curl_close($curl);
                ?>

            <?php
                #if(!empty($picture)){
                #    echo 'Picture:';
                #    foreach($picture as $post){
                #    echo '<img src= "'. $post["download_url"] .'" />';
                #    }
                #}
            ?>
    </body>
</html>
