const db_users = require("../db/db_users_service");
const utils = require("../utils");

function loginController(app) {
    app.post("/login", ((req, res) => {
        utils.printReqSummary(req)
        const user = req.body
        if (utils.validateUser(user)) {
            db_users.getUserByLogin(user.login).then((result) => {
                if (result !== undefined) {
                    if (user.password === result.password) {
                        return res.status(200).send()
                    } else {
                        return res.status(404).send({error: 'Invalid password'})
                    }
                } else {
                    return res.status(404).send({error: 'Data not found'})
                }
            })
        } else {
            return res.status(404).send({error: 'Invalid user data'})
        }
    }))
}

module.exports = {
    loginController: loginController
}
