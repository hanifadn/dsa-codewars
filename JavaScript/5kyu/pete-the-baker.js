/**
 * Title: Pete, the baker
 * Link: https://www.codewars.com/kata/525c65e51bf619685c000059
 * Difficulty: 5 kyu
 *
 * ## Description
 *
 * Given a recipe object (ingredient -> amount per cake) and available amounts, return how many
 * whole cakes you can bake. Missing ingredients count as 0.
 */

function cakes(recipe, available) {
  let minCakes = Infinity;
  for (const [ingredient, need] of Object.entries(recipe)) {
    if (need === 0) continue;
    const have = Object.prototype.hasOwnProperty.call(available, ingredient)
      ? available[ingredient]
      : 0;
    const n = Math.floor(have / need);
    if (n < minCakes) minCakes = n;
  }
  return minCakes === Infinity ? 0 : minCakes;
}
