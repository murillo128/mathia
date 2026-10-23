# MI-102 — Centered dyadic variance recovers full reciprocal-zeta principal parts

**Evidence level:** supported conditional synthesis of [MC-522](../../findings/MC-522-centered-dyadic-variance-recovers-all-reciprocal-zeta-poles.md). The variance premise is unproved. The transfer from [Prime Lattice MI-065](../../../prime_lattice/mind/intuition/MI-065-seam-filtering-recovers-sparse-arithmetic-poles-from-dyadic-variance.md) uses classical deconvolution and zero density; no external novelty or formal verification is claimed.

Fix `0<theta<1`, `X_j=2^j`, `H_j=floor X_j^theta`, and `S_j(y)=M(y+H_j)-M(y)`. Let `m_j=X_j^(-1)int_(X_j)^(2X_j)S_j(y)dy`. If, for every `epsilon>0`,

`V_j=int_(X_j)^(2X_j)|S_j(y)-m_j|^2dy <<_(theta,epsilon) X_j^(1+epsilon)H_j`

at every sufficiently large integer `j`, then `zeta(s)` has no zeros in `Re s>alpha=1-theta/2`, and `M(x)<<_(theta,epsilon)x^(alpha+epsilon)`. No bound on the means, other starting scales, neighboring lengths, zero multiplicities or residue signs is needed. The last conclusion uses the zeta-specific reciprocal-growth/Perron bridge in [MI-101](MI-101-smooth-deconvolution-separates-zero-exclusion-from-endpoint-recovery.md), not generic sharp inversion.

Put `tau=2pi/log 2`. Choose fixed integers `N,m` with `N(1-theta)>theta/2` and `2m>N`, and write

`q_m(t)=(1-cos(tau t))^m=sum_(ell=-m)^m d_ell exp(i ell tau t)`,

`d_ell=2^(-m)(-1)^ell binom(2m,m+ell)`.

The zero-extended weight `w_s(u)=q_m(log u)u^(-s)` on `[1,2]` is `C^N`. A finite differential inverse of the box average keeps its support and integral `J_m(s)=int_1^2 w_s(u)du`. With `b_j=X_j m_j/H_j`, the exact window identity and Cauchy--Schwarz give

`W_j(s)=sum_(X_j<n<=2X_j)mu(n)w_s(n/X_j)=b_j J_m(s)+R_j(s)`,

`|R_j(s)| << sqrt(X_j V_j)/H_j + X_j(H_j/X_j)^N << X_j^(alpha+delta)`

for every `delta>0`, locally uniformly in `s`. Summing the blocks for `D=1/zeta` yields

`D_m(s):=sum_ell d_ell D(s-i ell tau)=Q_m(s)+J_m(s)F(s)+G(s)`.

Here `Q_m` is entire, `G` is holomorphic on `Re s>alpha`, and `F(s)=sum_(j>=j_0)b_j 2^(-js)` starts on `Re s>1` and has period `i tau`. Crucially, `J_m(s)` has no zeros for `Re s<1`. The meromorphic continuation of `D` therefore continues `F` with its period intact. A pole of `F` in `alpha<Re s<1` would force a whole vertical progression of poles of `D_m`, contradicting the arithmetic bound `N_zeta(sigma,T)=o(T)` for each fixed `sigma>1/2`. Hence `D_m` is holomorphic there.

To undo the filter, retain **the whole principal part**, not just the residue. On a progression `rho+ik tau`, let `P_k(z)` be the finite Laurent principal part of `D(rho+ik tau+z)`. Then

`sum_ell d_ell P_(k-ell)=0` for every integer `k`.

Sparse pole support supplies `2m` consecutive zero principal parts; otherwise every block of that length would contain a pole. Since `d_(-m)` and `d_m` are nonzero, the recurrence propagates that zero block in both directions. Thus every `P_k` vanishes. Equivalently each Laurent coefficient is a polynomial sequence of degree at most `2m-1`, incompatible with sparse nonzero support. This works even for a multiple pole with zero residue, with no uniform degree bound on the principal parts. Every zeta zero is a genuine pole of its exact reciprocal.

The two rigidity inputs are separate. For `2/3<theta<1`, `alpha<beta<3/2-theta` and `0<c<1/4`, the positive dyadic density `dnu=c_j dx`, `c_j=1/4-c2^(j(beta-1))` on `[2^j,2^(j+1))`, `j>=0`, has

`V_j^nu=(c_(j+1)-c_j)^2(H_j^3/3-H_j^4/(4X_j))=o(X_j H_j)`

but poles at every `beta+ik tau`. It passes the centered variance ceiling and fails pole sparsity. This is a continuous-source control, not a Möbius example.

Every sufficiently large dyadic scale and the complete integral over starts remain necessary premises of this argument. Arbitrary selected shells or unpaid exceptional starts do not supply them. A family of fixed `theta` tending to `1`, each with its own constants, is equivalent to RH together with MC-520's converse and contraction under centering. No moving-exponent limit, boundary-line exclusion or unconditional variance estimate follows.
