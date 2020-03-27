package com.jisuan;

public class main {

	public static void main(String[] args) {
		LocationUtils a=new LocationUtils();
		double distance = a.getDistance(39.85789,116.37497,39.87979,116.35753);
		System.out.println("æ‡¿Î" + distance / 1000 + "π´¿Ô");
	}

}
