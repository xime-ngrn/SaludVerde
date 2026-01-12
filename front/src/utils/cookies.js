import Cookies from 'js-cookie'

const TOKEN_KEY = 'username'
const USER_KEY = 'nombres'

export function setAuthCookies(token, name) {
  Cookies.set(TOKEN_KEY, token, { expires: 1, sameSite: 'Lax' })
  Cookies.set(USER_KEY, name, { expires: 1, sameSite: 'Lax' })
}

export function getAuthToken() {
  return Cookies.get(TOKEN_KEY)
}

export function getUserName() {
  return Cookies.get(USER_KEY)
}

export function isAuthenticated() {
  return !!Cookies.get(TOKEN_KEY)
}

export function clearAuthCookies() {
  Cookies.remove(TOKEN_KEY)
  Cookies.remove(USER_KEY)
}
