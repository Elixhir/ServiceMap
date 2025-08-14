import React, { useState } from 'react';
import { View, Text, TextInput, TouchableOpacity, StyleSheet } from 'react-native';

export default function LoginScreen({ navigation }) {
  const [email, setEmail] = useState('');
  const [password, setPassword] = useState('');

  return (
    <View style={styles.container}>
      <Text style={styles.title}>Welcome Back!</Text>

      <TextInput
        style={styles.input}
        placeholder="Email"
        value={email}
        onChangeText={setEmail}
      />

      <TextInput
        style={styles.input}
        placeholder="Password"
        secureTextEntry
        value={password}
        onChangeText={setPassword}
      />

      <TouchableOpacity style={styles.button}>
        <Text style={styles.buttonText}>Sign In</Text>
      </TouchableOpacity>

      <TouchableOpacity style={styles.link}>
        <Text>Forgot Password</Text>
      </TouchableOpacity>

      <TouchableOpacity
        style={styles.link}
        onPress={() => navigation.navigate('Register')}
      >
        <Text>Create Account</Text>
      </TouchableOpacity>

      <TouchableOpacity style={styles.googleButton}>
        <Text>Sign up with Google</Text>
      </TouchableOpacity>
    </View>
  );
}

const styles = StyleSheet.create({
  container: { flex: 1, backgroundColor: '#fff', padding: 20, justifyContent: 'center' },
  title: { fontSize: 26, fontWeight: '600', textAlign: 'center', marginBottom: 35 },
  input: { backgroundColor: '#E5E7EB', padding: 12, borderRadius: 8, marginBottom: 25 },
  button: { backgroundColor: '#1E90FF', padding: 15, borderRadius: 25, alignItems: 'center', marginBottom: 25 },
  buttonText: { color: '#fff', fontWeight: '600', fontSize: 16 },
  link: { backgroundColor: '#F3F4F6', padding: 12, borderRadius: 25, alignItems: 'center', marginBottom: 20 },
  googleButton: { borderColor: '#ccc', borderWidth: 1, padding: 12, borderRadius: 25, alignItems: 'center', marginTop: 15 },
});
