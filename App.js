import { NavigationContainer } from "@react-navigation/native";
import { createNativeStackNavigator } from "@react-navigation/native-stack";
import { useState } from "react";
import HomeScreen from "./screens/HomeScreen";
import ProfileScreen from "./screens/ProfileScreen";
import SettingsScreen from "./screens/SettingsScreen";
import ConnectGroupScreen from "./screens/ConnectGroupScreen";
import MinistryTeamScreen from "./screens/MinistryTeamScreen";
import RegisterScreen from "./screens/RegisterScreen";
import LoginScreen from "./screens/LoginScreen";

const Stack = createNativeStackNavigator();

export default function App() {
  const [user, setUser] = useState(false);
  // const [user, setUser] = useState({
  //   id: 12345,
  //   name: "Jeffrey Rujen",
  //   mobile: 9043843538,
  //   email: "jeffrey.rujen@gmail.com",
  //   dateOfBirth: "15/09/2000",
  //   age: 22,
  //   gender: "Male",
  //   address:
  //     "006 A block, Sai Sunshine Apartment, Munnekollal, Bangalore - 560037",
  //   currentStage: "Foundation 101",
  //   interactionStartDate: "",
  //   inviteDate: "",
  //   followUpStartDate: "",
  //   plantedDate: "",
  //   baptized: true,
  //   connectGroupLeader: "Ps Michael Praveen",
  //   connectGroupPTL: "",
  //   connectGroupRole: "PTL",
  //   ministryTeam: "Videography",
  //   ministryTeamLeader: "Preethi",
  //   ministryTeamRole: "Trainer (streaming)",
  //   // TODO: Foundation 101, Alpha, Bible Study
  //   // TODO: 5 developmental tracks
  // });

  return (
    <NavigationContainer>
      {user ? (
        <Stack.Navigator>
          <Stack.Screen name="Home" options={{ title: `Hi ${user.name}` }}>
            {(props) => <HomeScreen {...props} userData={user} />}
          </Stack.Screen>
          <Stack.Screen name="Profile" component={ProfileScreen} />
          <Stack.Screen name="Settings" component={SettingsScreen} />
          <Stack.Screen name="ConnectGroup" component={ConnectGroupScreen} />
          <Stack.Screen name="MinistryTeam" component={MinistryTeamScreen} />
        </Stack.Navigator>
      ) : (
        <Stack.Navigator>
          <Stack.Screen name="Login" options={{ title: "Login" }}>
            {(props) => <LoginScreen {...props} setUser={setUser} />}
          </Stack.Screen>
          <Stack.Screen name="Register" options={{ title: "Register" }}>
            {(props) => <RegisterScreen {...props} setUser={setUser} />}
          </Stack.Screen>
        </Stack.Navigator>
      )}
    </NavigationContainer>
  );
}
