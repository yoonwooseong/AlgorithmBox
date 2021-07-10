
import java.util.ArrayList;
import java.util.List;
import java.util.Scanner;
import java.util.stream.IntStream;

public class nhnTest1 {

	private static void solution(int numOfAllPlayers, int numOfQuickPlayers, char[] namesOfQuickPlayers, int numOfGames,
			int[] numOfMovesPerGame) {
		// TODO: 이곳에 코드를 작성하세요. 추가로 필요한 함수와 전역변수를 선언해서 사용하셔도 됩니다.
		int[] score = new int[numOfAllPlayers];
		score[0] = 1;
		int[] person = new int[numOfAllPlayers - 1];
		int[] quickperson = new int[numOfQuickPlayers];
		int imposter = 'A';
		int position = 0;
		for (int i = 0; i < quickperson.length; i++) {
			quickperson[i] = namesOfQuickPlayers[i];
		}

		for (int i = 0; i < person.length; i++) {
			person[i] = 'B' + i;
		}

		for (int i = 0; i < numOfGames; i++) {
			position = play(person, numOfMovesPerGame[i], position);
			int num = person[position];

			if (IntStream.of(quickperson).anyMatch(x -> x == num)) {

			} else {
				int temp = person[position];
				person[position] = imposter;
				imposter = temp;
			}
			point(imposter, score);
		}

		// 결과 출력
		for (int i = 0; i < person.length; i++) {
			System.out.printf("" + (char) person[i] + " " + score[person[i] - 65]);
			System.out.println();
		}
		System.out.printf("" + (char) imposter + " " + score[imposter - 65]);
	}

	private static int play(int arr[], int move, int position) {
		if (position + move < 0) {
			while (true) {
				if (position + move < 0) {
					move += arr.length;
				} else {
					break;
				}
			}
		}
		position = (position + move) % arr.length;
		System.out.println(position);
		return position;
	}

	private static void point(int imposter, int[] score) {
		score[imposter - 65] += 1;
	}

	// https://gyoogle.dev/blog/computer-science/data-structure/Array.html

	private static class InputData {
		int numOfAllPlayers;
		int numOfQuickPlayers;
		char[] namesOfQuickPlayers;
		int numOfGames;
		int[] numOfMovesPerGame;
	}

	private static InputData processStdin() {
		InputData inputData = new InputData();

		try (Scanner scanner = new Scanner(System.in)) {
			inputData.numOfAllPlayers = Integer.parseInt(scanner.nextLine().replaceAll("\\s+", ""));

			inputData.numOfQuickPlayers = Integer.parseInt(scanner.nextLine().replaceAll("\\s+", ""));
			inputData.namesOfQuickPlayers = new char[inputData.numOfQuickPlayers];
			System.arraycopy(scanner.nextLine().trim().replaceAll("\\s+", "").toCharArray(), 0,
					inputData.namesOfQuickPlayers, 0, inputData.numOfQuickPlayers);

			inputData.numOfGames = Integer.parseInt(scanner.nextLine().replaceAll("\\s+", ""));
			inputData.numOfMovesPerGame = new int[inputData.numOfGames];
			String[] buf = scanner.nextLine().trim().replaceAll("\\s+", " ").split(" ");
			for (int i = 0; i < inputData.numOfGames; i++) {
				inputData.numOfMovesPerGame[i] = Integer.parseInt(buf[i]);
			}
		} catch (Exception e) {
			throw e;
		}

		return inputData;
	}

	public static void main(String[] args) throws Exception {
		InputData inputData = processStdin();

		solution(inputData.numOfAllPlayers, inputData.numOfQuickPlayers, inputData.namesOfQuickPlayers,
				inputData.numOfGames, inputData.numOfMovesPerGame);
	}
}
