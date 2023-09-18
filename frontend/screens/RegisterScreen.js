import { Button, StyleSheet, Text, TextInput, View } from "react-native";
import { StatusBar } from "expo-status-bar";

const RegisterScreen = ({ navigation, setUser }) => {
  return (
    <View style={styles.screen}>
      <TextInput style={styles.textInput} placeholder="Name" />
      <TextInput style={styles.textInput} placeholder="Mobile" />
      <TextInput style={styles.textInput} placeholder="Email" />
      <TextInput style={styles.textInput} placeholder="Date of Birth" />
      <TextInput style={styles.textInput} placeholder="Gender" />
      <TextInput style={styles.textInput} placeholder="Password" />
      <TextInput style={styles.textInput} placeholder="Confirm Password" />
      <Button
        style={styles.button}
        title="Register"
        onPress={() => setUser({})}
      />
      <Button
        style={styles.button}
        title="Login"
        onPress={() => navigation.replace("Login")}
      />
    </View>
  );
};

export default RegisterScreen;

const styles = StyleSheet.create({
  screen: {
    flex: 1,
    alignItems: "center",
    justifyContent: "center",
  },
  textInput: {
    padding: 16,
    margin: 4,
    borderBottomWidth: 1,
    borderColor: "#ccc",
    borderRadius: 4,
  },
  button: {
    margin: 4,
    paddingHorizontal: 16,
    paddingVertical: 8,
    borderRadius: 4,
  },
});
