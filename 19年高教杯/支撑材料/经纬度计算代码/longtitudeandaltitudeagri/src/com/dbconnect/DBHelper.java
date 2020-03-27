package com.dbconnect;
package com.baidu.ai.dbconnect;

import java.sql.Connection;
import java.sql.DriverManager;
import java.sql.SQLException;

/**
 * ���ڽ������ݿ����ӵ���
 */
public class DBHelper {

	private static final String DB_CONN_RUL = "jdbc:mysql://localhost:3306/DishData?serverTimezone=UTC";
	private static final String DB_USER_NAME = "root";
	private static final String DB_PASSWORD = "920691910";

	/**
	 * ���һ������, �������ݿ�
	 * 
	 * @return connection�����
	 */
	public static Connection getConnection() {
		Connection connection = null;
		try {
			// ��������
			Class.forName("com.mysql.cj.jdbc.Driver");
			// ��������
			connection = DriverManager.getConnection(DB_CONN_RUL, DB_USER_NAME, DB_PASSWORD);
		} catch (SQLException e) {
			e.printStackTrace();
		} catch (ClassNotFoundException e) {
			e.printStackTrace();
		}
		return connection;
	}
}
