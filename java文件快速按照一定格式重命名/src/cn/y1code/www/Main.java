package cn.y1code.www;

import java.io.File;

public class Main {


	public static void main(String[] args) {
		// TODO Auto-generated method stub
		File path = new File("img");
		File[] next = path.listFiles();
		rename(next);
		
	}
	public static void rename(File[] next) {
		for(int i = 0;i<next.length;i++){
			File re = new File("img/img " + i + ".jpg");
//			System.out.println(next[i].getName());
			next[i].renameTo(re);
			
		}
		System.out.println("重命名成功！");
		
	}
}
