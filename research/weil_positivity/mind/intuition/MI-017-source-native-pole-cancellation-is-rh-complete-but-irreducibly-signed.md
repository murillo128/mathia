# MI-017 — Source-native pole cancellation is RH-complete but irreducibly signed

**Evidence level:** supported by [WP-290](../../findings/WP-290-critical-mangoldt-dilation-coboundary-is-rh-equivalent-and-jordan-parts-remain-nontempered.md), together with the positive-completion obstructions of WP-288--WP-289. No Weil-positivity proof is claimed.

The signed source transformation demanded after WP-289 can be made completely intrinsic. For the critical Mangoldt half-density

`mu=sum_(n>=2) Lambda(n)/sqrt(n) delta_(log n)`

and any integer `q>=2`, define the multiplicative dilation coboundary

`Delta_q mu = mu - sqrt(q) S_(log q) mu`.

Its Laplace transform acquires the factor `1-q^(1/2-s)`. This cancels the zeta pole at `s=1/2` exactly, without adjoining a separate continuous pole sector, but it does not cancel poles from nontrivial zeros. WP-290 proves the exact category statement

`Delta_q mu in S'(R) <=> RH`.

The transformation therefore exposes a source-native RH-complete remainder rather than solving it. A matched nonarithmetic counting measure becomes tempered under the same coboundary unconditionally, so integer dilation differencing itself is only generic pole removal; the arithmetic content is the growth of the post-cancellation Mangoldt remainder.

More importantly for positivity, the cancellation is irreducibly signed. Both Jordan parts `(Delta_q mu)_+` and `(Delta_q mu)_-` are individually non-tempered. Taking absolute value, total variation, or preserving the positive and negative channels as separate positive summands destroys the category descent. This is a concrete realization of the source-side requirement in MI-016: the critical source must be changed before positivity is read, and the change may rely on cancellation that no componentwise positive completion can retain.

The remaining Weil question is not to find a pole-killing multiplier; one already exists inside the arithmetic semigroup. It is to embed this or another signed source-native remainder into a globally admissible construction whose final quadratic readout satisfies the exact Weil identities without assuming the RH-equivalent temperedness one is trying to prove.

**Boundary.** WP-290 does not show that this specific coboundary is the right intermediate object for a Weil construction. Its temperedness is already equivalent to RH, so treating it as an admissible distribution without an independent argument would be circular.