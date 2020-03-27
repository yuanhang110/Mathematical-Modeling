package com.dbconnect;
package com.baidu.ai.dbconnect;

import java.sql.Connection;
import java.sql.DriverManager;
import java.sql.SQLException;

/**
 * 用于建立数据库连接的类
 */
public class DBHelper {

	private static final String DB_CONN_RUL = "jdbc:mysql://localhost:3306/DishData?serverTimezone=UTC";
	private static final String DB_USER_NAME = "root";
	private static final String DB_PASSWORD = "920691910";

	/**
	 * 获得一个连接, 连接数据库
	 * 
	 * @return connection类对象
	 */
	public static Connection getConnection() {
		Connection connection = null;
		try {
			// 加载驱动
			Class.forName("com.mysql.cj.jdbc.Driver");
			// 生成连接
			connection = DriverManager.getConnection(DB_CONN_RUL, DB_USER_NAME, DB_PASSWORD);
		} catch (SQLException e) {
			e.printStackTrace();
		} catch (ClassNotFoundException e) {
			e.printStackTrace();
		}
		return connection;
	}
}
