# XF-210 — separated pair clouds in sublinear edge layers have vanishing adverse variation

**Status:** `EXACT-DERIVED` + `MATCHED-CONTROL` + `STRUCTURAL/DYNAMIC`.

The isolated-pair conclusion of XF-209 survives a growing number of
interacting close pairs. Fix \(0<\theta<1\). Put \(m=m_M\ge1\) defects
in the first \(M^\theta\) indices of a width-\(M\) smooth taper, with a
sufficiently large fixed index separation between defects. Their gaps
may be arbitrarily small and different. For the complete periodic heat
flow constructed below, there is an absolute \(T_*>0\) such that
\[
\boxed{\int_0^{T_*}(\mathcal K_a'(t))_-\,dt
 \le C_{A,\theta}m^2M^{-3}=o(1).}
\tag{1}
\]
Here \(v_-:=\max\{-v,0\}\), and the bound is uniform in all initial
small gaps. No independence or superposition of the nonlinear flows
is assumed. Only a comparison **supersolution** is superposed.

All potentially nonvanishing variation is again positive initial
logarithmic production. Its exact mass is
\[
E_M:=2\sum_{k\in P_M}W_k\log(1/\epsilon_k),
\qquad W_k=a_{k-1}+a_k.
\tag{2}
\]
For every fixed \(0<T\le T_*\), both total variation and net change
equal \(E_M+O_{A,\theta,T}(m^2M^{-3})\). Thus adding separated pairs
in a power-sublinear edge layer cannot turn XF-208's instantaneous
spikes into a persistent adverse integral. Colliding clusters without
the separation hypothesis, defects throughout a macroscopic part of
the taper, and source-driven replenishment remain outside this result.

## 1. Complete flow and quantifiers

Choose fixed absolute constants \(R\) and then \(D\gg R\gg1\), large
enough for the packing estimates in Section 3. Let \(N=8M\), and let
\[
P_M\subset\{0,\ldots,\lfloor M^\theta\rfloor\},\qquad
|P_M|=m\ge1,\qquad |k-\ell|\ge D\quad(k\ne\ell).
\tag{3}
\]
For sufficiently large \(M\), the periodic copies also have separation
at least \(D\). Choose arbitrary \(0<\epsilon_k\le\epsilon_*\), where
\(\epsilon_*>0\) is an absolute small constant. Set
\[
u_{k+1}(0)=u_{k+2}(0)=1-\epsilon_k\quad(k\in P_M),
\qquad u_i(0)=0\text{ at every other residue},
\]
and \(b_i=i-u_i(0)\), \(0\le i<N\). The roots are extended by
\(x_{i+N}(0)=x_i(0)+N\). At each defect the only changed gaps are
\[
g_k(0)=\epsilon_k,\qquad g_{k+1}(0)=1,\qquad
g_{k+2}(0)=2-\epsilon_k.
\tag{4}
\]
All other gaps are one. Define the real-entire heat flow
\[
f_t=e^{-t\partial_z^2}\prod_{i=0}^{N-1}
       \sin\frac{\pi(z-b_i)}N.
\tag{5}
\]
This is a finite Fourier sum, with every periodic image retained.

Let \(A\in C_c^\infty(\mathbb R)\) be fixed, nonnegative, supported
on \([0,3]\), positive on \((0,3)\), bounded by one, and equal to one
on \([1,2]\). Put \(a_j=A((j+1)/M)\). In particular \(a_j=0\) for
\(j<0\), and the plateau has pair coverage two. The profiles of
XF-208 satisfy these conditions after choosing positive smooth joins.
Use the XF-030 observable
\[
\mathcal J_j=J(g_j,g_{j+1}),\qquad
J(p,q)=2\log p+2\log q+2\log(p+q)
 -3\log\!\left[\frac23(p^2+pq+q^2)\right],
\qquad \mathcal K_a=\sum_j a_j\mathcal J_j.
\tag{6}
\]
The constants \(D,\epsilon_*,T_*\) do not depend on \(M,m,P_M\), or
the gaps. The error constants may depend on \(A,\theta\), and, where
stated, the fixed positive observation time \(T\).

## 2. Uniform continuation with all pair interactions present

For \(u_i=i-x_i\), subtracting the integer-lattice field gives
\[
u_i'=2\sum_{l\ne i}
 \frac{u_l-u_i}{(i-l)(i-l-u_i+u_l)}.
\tag{7}
\]
The sum runs over the full integer line and is absolutely convergent;
same-residue images have zero numerator. This is the lattice-subtracted
form of the exact cotangent velocity
\[
x_i'=\frac{2\pi}{N}\sum_{0\le l<N,\ l\ne i}
                   \cot\frac{\pi(x_i-x_l)}N.
\tag{8}
\]
The ordered finite periodic system is cooperative in \(u\), and every
constant \(u_i=c\) is stationary. The maximum principle gives
\(0\le u_i(t)\le1\) while the roots remain ordered. Hence gaps are
at most two and \(|x_i-x_l|\ge |i-l|-1\).

Bootstrap that all gaps except those indexed by \(P_M\) and its copies
are at least \(1/2\), and all exceptional gaps are small. Every root
outside a close pair has uniformly bounded velocity, by (7) and
summability of \((i-l)^{-2}\). At each pair,
\[
x_k'=-2/g_k+O(1),\qquad x_{k+1}'=2/g_k+O(1).
\tag{9}
\]
The constants are independent of the number of other pairs: after
removing the mutual pole, the nearest exterior distances have a fixed
lower bound and the distant bounds are indexed by \(|i-l|-1\).
The same reasoning bounds the exterior field derivative. In particular
\[
q_k':=(g_k^2)'=8-4q_kS_k,\qquad
S_k=\sum_{z\notin\{x_k,x_{k+1}\}}
 \frac1{(x_k-z)(x_{k+1}-z)},\qquad 0\le S_k\le C.
\tag{10}
\]
Every exterior root lies outside the adjacent pair. This supplies the
sign even though those exterior roots include other close pairs.
For small absolute \(\epsilon_*,T_*\),
\[
4\le q_k'\le8,\qquad
\epsilon_k^2+4t\le q_k(t)\le\epsilon_k^2+8t.
\tag{11}
\]
Pair centers move by \(O(t)\); pair roots move by \(O(t+\sqrt t)\);
all other roots move by \(O(t)\). These estimates hold simultaneously
for every pair. Every ordinary initial gap is at least one, so a
smaller absolute \(T_*\) makes all ordinary gaps at least \(3/4\).
This closes the bootstrap uniformly.

For each finite \(M\) and each set of positive initial gaps, the ODE
therefore continues on \([0,T_*]\) without collision. It agrees with
the roots of (5) by implicit differentiation and uniqueness.
Multiplying (5) by \(e^{\pi iz}\) gives a degree-\(N\) polynomial in
\(e^{2\pi iz/N}\) with nonzero extreme coefficients. The \(N\) continued
simple real roots per period exhaust its roots, proving that the
control is complete on the common interval.

## 3. A superposed spatial barrier, uniform in the number of pairs

Let \(\rho_N(i,c)\) be circular index distance modulo \(N\), and set
\[
b_i^{(k)}=2(1+\rho_N(i,k+3/2)/R)^{-2},\qquad
B_i=\sum_{k\in P_M}b_i^{(k)}.
\tag{12}
\]
The inverse-square convolution estimate proved in XF-209, Section 3,
is translation invariant, so for every center
\[
\sum_{l\ne i}\frac{b_l^{(k)}}{(i-l)^2}\le C_R b_i^{(k)}.
\]
Summing this **linear inequality** gives
\[
\sum_{l\ne i}\frac{B_l}{(i-l)^2}\le C_R B_i.
\tag{13}
\]
For clarity, the single-center estimate is uniform in \(N\): split
residues at half the distance from \(i\) to the center. In the far-center
part use the inverse-square kernel's bounded row sum; in the near-center
part use the profile's bounded mass \(O_R(1)\) and the kernel's
inverse-square decay. Same-residue images add \(O(N^{-2})b_i^{(k)}\).

Separation in (3) is needed for a different estimate. Packing centers
at distance at least \(D\), and integrating the decreasing profiles,
gives
\[
\sup_i B_i\le C(1+R/D),\qquad
\sup_i|B_{i+1}-B_i|\le C(R^{-1}+D^{-1}),\qquad
\sum_{i\bmod N}B_i\le C_Rm.
\tag{14}
\]
For the middle bound use
\(|\partial_s[2(1+s/R)^{-2}]|=(4/R)(1+s/R)^{-3}\).
On each side of an index, the ordered center distances increase by
at least \(D\); the sum of the derivative profiles is bounded by its
first term plus \(D^{-1}\) times its integral. Crossing a center or
the antipodal point is handled by integrating the same one-sided
bound across the unit interval. This proves (14) with absolute
constants, rather than a factor \(m/R\).

Choose fixed \(R,D\) so that the middle bound is below \(1/8\).
Let \(U_i(t)=e^{Lt}B_i\), \(L\ge4C_R\), and reduce \(T_*\) so that
\(e^{LT_*}\le2\). Then \(|U_{i+1}-U_i|<1/4\), so the hypothetical
roots \(i-U_i\) are ordered. Evaluating (7) at \(U\), discarding its
negative summands and using its gap floor, yields
\[
\text{right side of (7) at }U
 \le4e^{Lt}\sum_{l\ne i}\frac{B_l}{(i-l)^2}
 \le L e^{Lt}B_i=U_i'.
\tag{15}
\]
Initially \(B\ge u\). Cooperative comparison gives
\(0\le u_i(t)\le2B_i\). At first contact the self coordinate agrees
and all other coordinates are ordered; the off-diagonal derivatives
of the field are positive. A strict supersolution followed by a
limit handles equality. The actual small-gap coefficients need not
be bounded for this comparison.

For roots outside the close pairs, (7), (13), and the ordinary gap
floor now give \(|x_i'|\le C B_i\). Neighboring values of \(B\) are
comparable, uniformly, since this holds for every summand in (12).
Thus, in the taper range \(0\le j<3M\), outside the four triple starts
\[
H_k:=\{k-2,k-1,k,k+1\},\qquad H:=\bigcup_{k\in P_M}H_k,
\]
both \(|d_j|\) and \(|d_j'|\) are at most \(CB_j\), where
\(d_j=\log(g_{j+1}/g_j)\). Since \(J=F(d)\), \(F'(0)=0\), and all
these gaps belong to \([3/4,2]\),
\[
|\mathcal J_j'|\le C B_j^2\qquad(j\notin H).
\tag{16}
\]
This includes all triples that had equal gaps initially but evolve
under the combined field of the pair cloud.

## 4. Extracting the positive logarithms before estimating the remainder

The two triples containing \(g_k\) have
\[
\mathcal J_{k-1}=\log q_k+\mathcal R(g_k,g_{k-1}),\qquad
\mathcal J_k=\log q_k+\mathcal R(g_k,g_{k+1}),
\]
where symmetry of \(J\) is used and
\[
\mathcal R(g,h)=2\log h+2\log(g+h)
 -3\log\!\left[\frac23(g^2+gh+h^2)\right].
\tag{17}
\]
The first derivatives of \(\mathcal R\) are bounded for \(g\) in the small
closed range from (11) and \(3/4\le h\le2\). Their time derivatives
are \(O(1+1/g_k)\) by (9). The two remaining triples in \(H_k\)
have ordinary gaps but one singular-velocity root, so their derivatives
obey the same bound. The sets \(H_k\) are disjoint by (3). Also
\[
\int_0^T\frac{dt}{g_k(t)}\le\sqrt T
\qquad(0\le T\le T_*\le1).
\tag{18}
\]
Consequently the **full** derivative has the exact decomposition
\[
\boxed{\mathcal K_a'
 =\sum_{k\in P_M}W_k\frac{q_k'}{q_k}+r_M,}
\tag{19}
\]
with
\[
\int_0^T|r_M|\,dt\le C\left[
 \sqrt T\sum_{j\in H}a_j
 +T\sum_{j\notin H}a_jB_j^2\right].
\tag{20}
\]
The first sum in (19) is nonnegative. Estimating its absolute value
together with the remainder would unnecessarily require a lower-gap
bound; preserving its sign avoids that loss.

Let \(\ell=\lfloor M^\theta\rfloor+4\). Smoothness and support give
\(A(s)\le C_{A,r}s^r\) on \([0,3]\) for every integer \(r\ge1\).
On \(0\le j\le2\ell\), (14) gives
\[
\sum a_jB_j^2+\sum_{j\in H}a_j
 \le C_{A,r}m(\ell/M)^r,
\tag{21}
\]
where the first sum is restricted to that range and all nonzero
weights of \(H\) lie there. Here \(\sum B_j^2\le(\sup B)\sum B\le Cm\).
For \(2\ell<j<3M\), each center in (12) is at circular distance at
least a fixed multiple of \(j\), so \(B_j\le Cm(1+j)^{-2}\).
Using flatness with \(r=4\),
\[
\sum_{2\ell<j<3M}a_jB_j^2\le C_A m^2M^{-3}.
\tag{22}
\]
Choose an integer \(r\) with \(r(1-\theta)\ge3\). Equations
(20)--(22), \(m\ge1\), and \(T\le T_*\) imply
\[
\boxed{\int_0^T|r_M|\,dt\le C_{A,\theta}m^2M^{-3}.}
\tag{23}
\]
Since \(m\le1+M^\theta/D\), this tends to zero. The nonnegative term
in (19) proves (1).

## 5. Total variation and concentration have the same sign boundary

For fixed \(0<T\le T_*\), (11) bounds every \(q_k(T)\) above and
below by positive constants independent of \(k,M,\epsilon_k\).
Integrating the nonnegative term in (19) therefore gives
\[
\sum_k W_k\log\frac{q_k(T)}{\epsilon_k^2}
 =E_M+O_T\left(\sum_kW_k\right).
\]
Flatness, with the same \(r\) as above, bounds \(\sum W_k\) by
\(C_{A,\theta}mM^{-3}\). Thus
\[
\boxed{\begin{aligned}
\int_0^T|\mathcal K_a'|\,dt
 &=E_M+O_{A,\theta,T}(m^2M^{-3}),\\
\mathcal K_a(T)-\mathcal K_a(0)
 &=E_M+O_{A,\theta,T}(m^2M^{-3}).
\end{aligned}}
\tag{24}
\]
In particular absolute variation vanishes exactly when \(E_M\to0\).
If \(E_M\to E<\infty\), then on the **closed** interval \([0,T]\),
\[
\mathcal K_a'(t)\,dt\rightharpoonup E\delta_0.
\tag{25}
\]
Indeed the positive measure in (19) has total mass tending to \(E\),
and for every fixed \(0<\delta<T\) its mass on \([\delta,T]\) is at
most \(C_{\delta,T}\sum W_k=o(1)\). The remainder vanishes in total
variation by (23). Arbitrarily deep initial gaps can increase \(E_M\),
but cannot change this concentration to an adverse atom.

## 6. Prior art, stress tests, and the remaining Xi boundary

The reciprocal zero law and square-root opening are classical; see
[Tao's heat-flow exposition](https://terrytao.wordpress.com/2017/10/17/heat-flow-and-zeroes-of-polynomials/)
with the time sign reversed. The complete image sum is the classical
[cotangent partial fraction, DLMF 4.22.3](https://dlmf.nist.gov/4.22.E3).
Cooperative comparison and summable spatial barriers are classical
tools. [Guillin--Le Bris--Monmarche](https://www.numdam.org/articles/10.5802/jep.235/)
provides neighboring contraction and propagation-of-chaos theory for
one-dimensional singular particle systems; none of its stochastic or
mean-field estimates is used as the tapered deterministic theorem here.
[Rodgers--Tao, Section 9, Proposition 28](https://arxiv.org/pdf/1801.05914v5)
uses selected separating boundaries for a different localized energy.
It does not remove the spatial hypotheses in (3).

The line-local mathematical delta is uniformity in a **growing** number
of mutually interacting defects, with arbitrary distinct gap depths.
XF-209 supplies the one-center comparison kernel, but its conclusion
cannot simply be summed: the zero trajectories do not superpose.
Equations (13)--(16) instead establish an ordered many-center barrier
and retain the quadratic far-tail cost \(m^2\). Equations (19)--(23)
then control the adverse part without paying the logarithmic depths.
No literature-wide novelty or Xi-specific mechanism is claimed.

The proof tests the nonuniform points directly: ordinary-gap continuation
does not lose a factor \(m\); center packing keeps the comparison roots
ordered; the far tail includes every periodic image and every newly
evolving triple; both triples containing a small gap contribute to
\(W_k\); and no cancellation between positive and negative time mass
is used in bounding the remainder. The result is an analytic derivation,
not numerical trajectory evidence or a Lean-verified theorem.

Fixed separation and the power-sublinear location bound are essential
to the **proved estimate**. This does not assert they are necessary
for every possible positive theorem. The argument supplies no estimate
for adjacent multi-root clusters, defects spread through the taper
plateau, or continual incoming boundary disturbances. Nor does it give
a uniform backward interval: under physical root rescaling by \(h\),
the interval becomes \(h^2T_*\). The controls retain bounded lattice
displacement and upper gaps, but are not asserted to satisfy Xi's
arithmetic source law, even symmetry, or global counting asymptotic.
No bound on the de Bruijn--Newman constant follows.

The overlap/taper clue remains open. A persistent adverse-integral
example must escape this separated edge-cloud class, or a positive
Xi theorem must control the still-uncovered interior, clustering, and
source-time regimes.
