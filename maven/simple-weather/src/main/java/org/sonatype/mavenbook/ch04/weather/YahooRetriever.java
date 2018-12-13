package org.sonatype.mavenbook.ch04.weather;

import java.io.InputStream; 
import java.net.URL;
import java.net.URLConnection;

import org.apache.log4j.Logger;

public class YahooRetriever {
	private static Logger log = Logger.getLogger(YahooRetriever.class);
	public InputStream retrieve(int zipcode) throws Exception {
		log.info( "Retrieving Weather Data" );
		String url = "https://weather-ydn-yql.media.yahoo.com/forecastrss?w=" + zipcode; URLConnection conn = new URL(url).openConnection();
		return conn.getInputStream();
	} 
}
