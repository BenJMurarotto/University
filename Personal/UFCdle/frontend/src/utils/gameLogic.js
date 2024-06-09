export const maxGuesses = 6;

export function checkGuess(fighter, secretFighter) {
  let attributes = ['fname', 'lname', 'nickname', 'rank', 'division', 'style', 'country', 'debut'];
  return attributes.map(attr => {
    return {
      attr,
      isMatch: fighter[attr] === secretFighter[attr]
    };
  });
}
