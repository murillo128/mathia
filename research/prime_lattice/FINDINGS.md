# Prime-lattice findings

This index contains only durable mathematical results that passed the `mathia-research-watch` substantive-finding gate. Detailed derivations and audits live in `findings/`.

## PL-001 — Bohr-Hardy evaluation boundary is `Re(s)=1/2`

**Evidence:** `LITERATURE+DERIVED`

For the Hedenmalm–Lindqvist–Seip Hilbert space of Dirichlet series with square-summable coefficients, point evaluation at `s = sigma + i t` is bounded exactly for `sigma > 1/2`, with evaluation norm squared `zeta(2 sigma)`. On the Bohr curve `z(s)=(p^{-s})_p`, the same threshold is the `ell^2` boundary `sum_p p^{-2 sigma}<infinity`. Thus the RH critical line is an exact natural boundary of this standard Hilbert-space geometry, although this fact alone says nothing about the location of zeta zeros.

Detailed note: [`PL-001-bohr-hardy-half-boundary.md`](findings/PL-001-bohr-hardy-half-boundary.md)

## PL-002 — Standard `H^2` kernel cannot see nontrivial zeta zeros

**Evidence:** `LITERATURE+DERIVED + DECISIVE-NEGATIVE`

The reproducing kernel is `K(s,w)=zeta(s+conj(w))` for `Re(s), Re(w)>1/2`. Hence `Re(s+conj(w))>1`, where the Euler product is zero-free. Therefore kernel zeros or orthogonality of standard Bohr-Hardy evaluation states cannot encode the nontrivial Riemann zeros. Any such route must leave or enlarge the standard reproducing-kernel setting.

Detailed note: [`PL-002-standard-h2-kernel-zero-obstruction.md`](findings/PL-002-standard-h2-kernel-zero-obstruction.md)

## PL-003 — Ambient prime torus does not rigidly determine a zero set

**Evidence:** `LITERATURE+DERIVED + DECISIVE-NEGATIVE`

Completely multiplicative unimodular twists `chi`, viewed as points of the infinite prime torus, preserve the same ambient character group and log-prime frequency structure but can have radically different analytic zero/pole behavior. Helson's random characters are almost surely analytic and zero-free for `Re(s)>1/2`, while Bochkov–Romanov construct Helson zeta functions with essentially arbitrary zeros and poles in a large part of the critical strip. Therefore a mechanism depending only on the undistinguished ambient torus or frequency list `log p` cannot determine the Riemann zero set; it must use additional structure that canonically singles out the Riemann case.

Detailed note: [`PL-003-ambient-prime-torus-zero-flexibility.md`](findings/PL-003-ambient-prime-torus-zero-flexibility.md)

## PL-004 — Prime-exponent gas is classical prior art

**Evidence:** `CLASSICAL-IDENTITY` — prior-art redirect

The occupation-number interpretation `v_p(n)` with one-particle energies `log p`, total energy `log n`, and partition function `zeta(beta)` is the classical free Riemann/primon gas of Julia. Bost–Connes subsequently built a richer `C*`-dynamical system with partition function zeta, and Connes developed a noncommutative adelic trace-formula interpretation of zeta zeros. The bare exponent-lattice statistical-mechanics interpretation is therefore not novel; prior art redirects attention toward what extra arithmetic/dynamical structure is added beyond the free lattice gas.

Detailed note: [`PL-004-prime-exponent-gas-prior-art.md`](findings/PL-004-prime-exponent-gas-prior-art.md)
