const getters = {
  token: state => state.user.token,
  refreshToken: state => state.user.refreshToken,
  user: state => state.user.user
}
export default getters
