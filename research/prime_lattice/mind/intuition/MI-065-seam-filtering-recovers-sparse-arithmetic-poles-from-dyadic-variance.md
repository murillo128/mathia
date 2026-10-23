# MI-065 — Seam filtering recovers sparse arithmetic poles from dyadic variance

**Evidence level:** supported conditional synthesis of [PL-466](../../findings/PL-466-dyadic-seam-weights-remove-the-variance-endpoint-loss.md). The prime variance input remains unproved. The deconvolution and zero-density tools are classical; no external novelty or formal verification is claimed.

Let `X_j=2^j`, `H_j=floor X_j^theta`, `0<theta<1`, and `a_n=Lambda(n)1_(n=1 mod 5)`. For `P_j(y)=sum_(y<n<=y+H_j)a_n` and its own mean `mu_j=X_j^(-1)int_(X_j)^(2X_j)P_j(y)dy`, suppose

`V_j=int_(X_j)^(2X_j)|P_j(y)-mu_j|^2dy << X_j H_j (log(2X_j))^A`

for every sufficiently large integer `j`, with fixed finite `A>=0`. Then all mod-5 Dirichlet L-functions are nonzero in `Re s>alpha=1-theta/2`. No mean estimate, other starting scale, or neighboring window length is required. The gain over sharp-block reconstruction is strict for `theta>2/3`.

The mechanism retains the seams rather than discarding neighborhoods of them. Put `tau=2pi/log 2`, choose fixed integers `N,m` with `N(1-theta)>theta/2` and `2m>N`, and use

`q_m(t)=(1-cos(tau t))^m=sum_(ell=-m)^m d_ell exp(i ell tau t)`,

`d_ell=2^(-m)(-1)^ell binom(2m,m+ell)`.

The zero-extended weight `w_s(u)=q_m(log u)u^(-s)` on `[1,2]` is `C^N`. A finite differential inverse of the box average preserves its support and integral, with residual `O((H_j/X_j)^N)`. Cauchy--Schwarz therefore gives, locally uniformly in `s`,

`sum_(X_j<n<=2X_j) a_n q_m(log(n/X_j))(n/X_j)^(-s) = b_j J_m(s)+O(X_j^alpha(log X_j)^B)`,

where `b_j=X_j mu_j/H_j`, `J_m(s)=int_1^2 q_m(log u)u^(-s)du`, and `B=max(A/2,1)`. The coefficient-weighted approximation error is `O(X_j(H_j/X_j)^N log X_j)`; the choice of `N` puts it below `X_j^alpha`. Vanishing endpoint jets, rather than a change in the available variance data, remove the boundary cost.

Write

`D(s)=(1/4)sum_(chi mod 5)(-L'/L)(s,chi)`,

`D_m(s)=sum_(ell=-m)^m d_ell D(s-i ell tau)`.

Summing the weighted blocks gives exactly `D_m=Q_m+J_m F+G`, where `Q_m` is entire, `G` is holomorphic in `Re s>alpha`, and `F(s)=sum_(j>=j_0)b_j 2^(-js)` is initially convergent for `Re s>1` and `i tau`-periodic. With `z=1-s`,

`J_m(s)=(2^(1-s)-1)(2m)! tau^(2m) / [2^m z product_(r=1)^m(z^2+r^2 tau^2)]`.

It is nonzero for `Re s<1`. Thus `F` continues meromorphically, preserving periodicity. Any pole in `alpha<Re s<1` would force a complete vertical progression of poles of `D_m`. Classical mod-5 zero density gives only `o(T)` zeros in each fixed half-plane `Re s>=sigma>1/2` up to height `T`, whereas a vertical progression has order `T` points. Hence `F` and `D_m` have no poles in this strip.

Filtered holomorphy is not yet enough: the finite filter could erase poles of `D`. On any progression `rho+ik tau` in the strip, put `r_k=Res_(s=rho+ik tau) D(s)`, including zero at regular points. Then

`r_k=-(1/4)sum_(chi mod 5) multiplicity_chi(rho+ik tau)`,

`sum_ell d_ell r_(k-ell)=0`.

The filter symbol is `(-1)^m 2^(-m)u^(-m)(u-1)^(2m)`, so `r_k` is a polynomial in `k` of degree at most `2m-1`. A nonzero polynomial is nonzero at all but finitely many integers; zero density instead gives only `o(K)` nonzero residues for `|k|<=K`. Thus every residue vanishes. The identity-residue weights ensure that coincident L-zeros cannot cancel in `D`. Classical nonvanishing on `Re s=1` and the Euler product to its right complete the claimed half-plane.

Both arithmetic steps matter. For `2/3<theta<1` and `alpha<beta<3/2-theta`, the positive measure `dnu(x)=c_j dx` on `[2^j,2^(j+1))`, `j>=0`, with `c_j=1/4-c 2^(j(beta-1))`, `0<c<1/4`, has

`V_j=(c_(j+1)-c_j)^2(H_j^3/3-H_j^4/(4X_j))=o(X_j H_j)`,

yet its Mellin transform has poles at every `beta+ik tau`. It passes the variance and seam-filter identities and fails the sublinear pole-count condition. Small dyadic variance alone does not exclude such generic positive sources.

A family of these estimates at fixed exponents tending to `1` implies joint GRH modulo 5, with constants depending on each exponent. No converse, boundary-line exclusion, sharp block-mass reconstruction, or covariance lower-frame estimate is proved. A sparse subsequence of dyadic scales does not supply the exact periodic decomposition.
