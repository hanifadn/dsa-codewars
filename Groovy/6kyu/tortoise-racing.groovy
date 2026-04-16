/**
 * Title: Tortoise racing
 * Link: https://www.codewars.com/kata/55e2adece53b4cdcb900006c
 * Difficulty: 6 kyu
 *
 * ## Description
 *
 * Tortoise A has speed v1 and tortoise B has speed v2 (feet per hour). When B starts, A has a lead of
 * g feet. How long until B catches A? Return [hour, min, sec] with whole seconds (floor). If v1 >= v2,
 * B never catches A — return null.
 */

class Kata {
	static List race(int v1, int v2, int g) {
		if (v1 >= v2)
			return null
		int totalSeconds = g * 3600 / (v2 - v1)
		int h = totalSeconds / 3600
		int m = (totalSeconds % 3600) / 60
		int s = totalSeconds % 60
		[h, m, s]
	}
}
