/*
 * Travessa.java
 * 
 * Copyright 2018 cf17eduard.corral <cf17eduard.corral@E-xxx>
 * 
 * This program is free software; you can redistribute it and/or modify
 * it under the terms of the GNU General Public License as published by
 * the Free Software Foundation; either version 2 of the License, or
 * (at your option) any later version.
 * 
 * This program is distributed in the hope that it will be useful,
 * but WITHOUT ANY WARRANTY; without even the implied warranty of
 * MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
 * GNU General Public License for more details.
 * 
 * You should have received a copy of the GNU General Public License
 * along with this program; if not, write to the Free Software
 * Foundation, Inc., 51 Franklin Street, Fifth Floor, Boston,
 * MA 02110-1301, USA.
 * 
 * 
 */


public class Travessa {
		
	public static int[][] generarPartits(int numeroPartits){
    		int [][] matriu = new int[numeroPartits][2];
    		for(int p=0;p<numeroPartits;p++){
			matriu[p][0]=(int) (Math.random()*4);
			matriu[p][1]=(int) (Math.random()*4);
		}
		return matriu;
	}	
		
	public static String pintaJornada(int[][] partits){
		String cadena="{";
		for(int p=0;p<partits.length-1;p++){
			cadena+="{"+partits[p][0]+",";
			cadena+=partits[p][1]+"},";
		}
		cadena+="{"+partits[partits.length-1][0]+",";
		cadena+=partits[partits.length-1][1]+"}}";
		return cadena;
	}
	
    	public static int calcularVictoriesVisitants(int[][] partits){
		int victories=0;
		for(int p=0;p<partits.length;p++){
			if(partits[p][0]<=partits[p][1]){
			    victories++;
			}
		}	
		return victories;
    	}
    	
    	public static float mitjaGolsPartit(int[][] partits){
    		int gols=0;
    		for(int p=0;p<partits.length;p++){
    			if(partits[p][0]+partits[p][1] > 0){
    			    gols += partits[p][0]+partits[p][1]; 
    			}
    			else {
    				gols = 2;
    			}
    		}	
    		return gols/partits.length;
    }
    	
}
