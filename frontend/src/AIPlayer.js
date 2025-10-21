export const aiMove = () => {
  const actions = ["move_forward", "move_backward"];
  return actions[Math.floor(Math.random() * actions.length)];
};
