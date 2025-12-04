import java.io.*;
import java.util.ArrayList;
import java.util.Scanner;

class Day3 {
	public static void main(String[] args) throws Exception { 
		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));

		System.out.print("Enter the text file to run: ");

		String path = br.readLine();

		File file = new File(path);
		
		Scanner sc = new Scanner(file);

		ArrayList<String> battery_banks = new ArrayList<>(); 
		while (sc.hasNextLine()) 
			battery_banks.add(sc.nextLine());

		System.out.println(part1(battery_banks));
	}

	public static int part1(ArrayList<String> battery_banks) {
		int totalOutput = 0;
		for (String bank : battery_banks) {

			// find the first max value and keep its index
			int max = 0;
			int first_idx = 0;
			for (int i = 0; i < bank.length(); ++i) {
				if (bank.charAt(i) - '0' > max) {
					max = bank.charAt(i) - '0';
					first_idx = i;
				}	
			}
			
			int secondMax = 0;
			String temp = "";
			if (first_idx + 1 > bank.length() - 1) {
				for (int i = first_idx - 1; i >= 0; --i) {
					if (bank.charAt(i) - '0' > secondMax)
						secondMax = bank.charAt(i) - '0';
				}
				temp = secondMax + "" + max;
			} else {
				for (int i = first_idx + 1; i < bank.length(); ++i) {
					if (bank.charAt(i) - '0' > secondMax)
						secondMax = bank.charAt(i) - '0';
				}
				temp = max + "" + secondMax;
			}
			int joltage = Integer.parseInt(temp);	
			totalOutput += joltage;
			
		}
		return totalOutput;
	}
}
