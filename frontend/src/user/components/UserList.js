import React from 'react';
import PropTypes from 'prop-types';
import { withStyles } from '@material-ui/core/styles';
import List from '@material-ui/core/List';
import ListItem from '@material-ui/core/ListItem';
import ListItemText from '@material-ui/core/ListItemText';
import Avatar from '@material-ui/core/Avatar';
import UserIcon from '@material-ui/icons/AccountCircle';

import {useSelector} from 'react-redux';

const styles = theme => ({
    root: {
        width: '100%',
        maxWidth: 360,
        backgroundColor: theme.palette.background.paper,
    },
});

function UserList(props) {

    const { classes, userIds } = props;
    const userData = useSelector(state=>state.user.users.byIds)

    return (
        <List className={classes.root}>
            {userData &&
            userIds.map((userId, i)=>(
                <ListItem>
                <Avatar>
                    <UserIcon />
                </Avatar>
                <ListItemText 
                    primary={userData[userId].displayname} 
                    secondary={userData[userId].entity.name}  />
                </ListItem>
            ))}
            {userData && userIds.length===0 && <div> No users </div>}
        </List>
    );
}

UserList.propTypes = {
    classes: PropTypes.object.isRequired,
};

export default withStyles(styles)(UserList);
