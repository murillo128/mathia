# MI-061 — Fixed-depth positive Vandermonde geometry is a partition-sum spectrum

**Evidence level:** exact finite-dimensional/measure-theoretic synthesis from [VIS-365](../../findings/VIS-365-finite-weighted-vandermonde-subset-energy-spectrum.md) and [VIS-366](../../findings/VIS-366-fixed-depth-vandermonde-partition-sum-spectrum.md), with the determinant identity supplied by the classical Andreief/Cauchy--Binet framework.

For fixed polynomial depth `q`, let `mu` be any positive probability measure on a compact interval `K` and let

`T_mu a(t)=sum_(d=0)^(q-1) a_d t^d`

map coefficient vectors into `L^2(mu)`. If `s_1>=...>=s_q` are its singular values, define

`Z_k(mu)=(1/k!) integral_(K^k) prod_(i<j)(x_j-x_i)^2 dmu(x_1)...dmu(x_k)`.

VIS-366 shows, for every `k` not exceeding the rank,

`prod_(r=1)^k s_r(mu) asymp_(q,K) sqrt(Z_k(mu))`,

and hence

`s_k(mu) asymp_(q,K) sqrt(Z_k(mu)/Z_(k-1)(mu))`.

At `k=q`, the product identity is exact because `Z_q(mu)=det(T_mu^*T_mu)`.

This removes support cardinality from the fixed-depth conditioning problem. The support of `mu` may grow without bound or be continuous; after normalization, all coefficient-side geometry still enters through one fixed `q x q` moment Gram. For discrete support `mu=sum_i pi_i delta_(t_i)`, the exact quantity is the positive partition sum

`Z_k(mu)=sum_(|I|=k) (prod_(i in I)pi_i) prod_(i<j; i,j in I)(t_j-t_i)^2`.

VIS-365 is the tropical specialization. When a fixed finite family has `sqrt(pi_i) asymp epsilon^(a_i)` and pair separations `|t_i-t_j| asymp epsilon^(kappa_ij)`, the least exponent among the terms of `Z_k` is

`Gamma_k=min_(|I|=k)[sum_(i in I)a_i+sum_(i<j)kappa_ij]`,

so `sqrt(Z_k) asymp epsilon^(Gamma_k)`. The finite subset-energy ledger is therefore not a separate mechanism; it is the hard-min limit of the exact partition sum.

The key closure is stronger than finite branching. At fixed `q`, adding arbitrarily many positive compact support points, taking a continuous positive limit, or replacing clean power scales by non-power/non-comparable compact scales does not create an unpriced conditioning resource. The full effect is already present in `Z_1,...,Z_q`, with comparison constants depending on `q` and `K` but not on support cardinality.

The reusable audit is now: form the normalized positive coefficient measure and price its Vandermonde partition sums before crediting support growth or clustering as arithmetic structure. A small singular value explained by `Z_k/Z_(k-1)` is source-free positive-Hilbert conditioning, even when many support subsets contribute and no single valuation dominates.

**Boundary.** The depth `q` is fixed and the normalized support remains in one compact interval. The theorem uses positive Hilbert/diagonal geometry; signed, indefinite or non-diagonal coefficient structures are outside it. The constants are not uniform in growing `q`, and noncompact support, source-dependent signed selectors, global phase/window effects, nonlinear dependence or genuinely growing-dimensional limits remain separate regimes. No stronger estimate for the Chebyshev-theta remainder or RH follows from this conditioning classification.
