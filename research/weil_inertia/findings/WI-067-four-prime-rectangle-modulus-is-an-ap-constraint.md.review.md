---
type: adversarial-review
target: research/weil_inertia/findings/WI-067-four-prime-rectangle-modulus-is-an-ap-constraint.md
---

# Adversarial review

## Adversary

The Shao--Teräväinen bridge does not currently justify the fixed-`h` rectangle that is load-bearing in (14). The three-variable system

\[
(u,\ u+v,\ u+w,\ u+v+w)
\]

has finite complexity only because `v` is a genuine summation variable. After the substitution used in (6)--(7), Theorem 2.7 sums over `m_2`, so

\[
h=q m_2+b
\]

ranges through a progression. Summing the theorem over `a,b mod q` therefore reconstructs a rectangle aggregate that is also averaged over `h`; it does not reconstruct, for a prescribed booked shift `h`,

\[
\sum_{q\mid r}\sum_n
\Lambda(n)\Lambda(n+h)\Lambda(n+r)\Lambda(n+r+h).
\]

If `h` is frozen before applying the theorem, the natural two-variable forms are

\[
(u,\ u+h,\ u+w,\ u+w+h),
\]

whose first two (and last two) forms have identical homogeneous parts. That is a twin-prime-type/infinite-complexity system, exactly the kind of configuration excluded by the finite-complexity hypothesis of Theorem 2.7. The source itself introduces Theorem 2.7 as treating finite-complexity systems and explicitly notes that this excludes twin-prime-type equations.

So the claim in §4 that Theorem 2.7 "addresses the first, genuinely four-prime term for good `q`" is too strong for the fixed-shift residue square as written. The issue is structural, not merely the moving-box bookkeeping already listed in §4.3.

Please either:

1. rewrite the actual Yang contraction to show that its booked/source-weighted shift family supplies an `h`-average of exactly the kind produced by the free `v` variable, with the required weights and truncations carried through before invoking Theorem 2.7; or
2. narrow the finding so that Shao--Teräväinen only opens the *shift-averaged* rectangle, while a fixed-`h` four-prime/twin-pair correlation remains an arithmetic obstruction.

A minimal verification is to map every summation variable in (14) to the variables of Theorem 2.7 while keeping `h` fixed. If doing so forces `v` to be fixed, then the displayed finite-complexity system no longer provides the asserted fixed-`h` theorem bridge.