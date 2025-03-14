import React from 'react';
import { Typography, Box } from '@mui/material';

const Footer: React.FC = () => {
  return (
    <Box mt={4} py={3} bgcolor="primary.main" color="white" textAlign="center">
      <Typography variant="body1">© 2023 Motorrad Inserate</Typography>
    </Box>
  );
};

export default Footer;