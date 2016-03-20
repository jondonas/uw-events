<?php
 class rss {
        var $feed;
        function rss($inputfeed){
            $this->feed = $inputfeed;
        }

        function parse(){
            $rss = simplexml_load_file($this->feed);

            $split = array();

            foreach ($rss->channel->item as $item) {

              $title = (string) $item->title; 
              $link   = (string) $item->link; 
              $pubDate   = (string) $item->pubDate; 
              $description = (string) $item->description; 

             $split[] = '
                    <li>
                        <h3><a href="'.$link.'">'.$title.'</a></h3>
                        <p>'.$description.'</p>
                        <a href="'.$link.'">Read More</a>
                    </li>
                    <br>
                ';
            }
            return $split;
        }

        function display($rownum,$title){

            $split = $this->parse();
            $i = 0;
            $rss_data = '<ul class="newsBlock">';
            while($i<$rownum){
              $rss_data .= $split[$i];
              $i++;
            }
            $trim = str_replace('', '',$this->feed);
            $user = str_replace('&lang=en-us&format=rss_200','',$trim);


            $rss_data.='</ul>';

            return $rss_data;
        }
}
?>
