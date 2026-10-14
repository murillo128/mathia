# FD-333 — One lattice quantum at fixed Farey-defect ranks permits macroscopic spectral separation

**Status:** EXACT-DERIVED + PNT/DIRICHLET-ASSISTED-ASYMPTOTIC + EXACT-RATIONAL-CHECKS + SHARP-INVERSE-STABILITY-BOUNDARY.

FD-331 shows that, for a fixed prime, the exact positions and values of all defective Hall--Shiu indices determine a whole-excursion reassembly. Its lattice observation gives rigidity if the ranks agree and every index-value error is strictly less than \(1/p\). The converse stability threshold is sharp: **one quantum \(1/p\), and not merely two, suffices to separate two reflected reassemblies by a nonzero limiting Franel energy and a fixed even sine mode**. This is a matched-control obstruction, not a theorem about alternative genuine Farey sequences.

## 1. Infinite-prime sharp-quantum theorem

Fix an integer \(v\ge3\), put \(u=v+1\), \(\alpha=1/u\), \(\beta=1/v\), and \(d=\beta-\alpha=1/(uv)>0\). By the Chinese remainder theorem and Dirichlet's theorem there are infinitely many primes satisfying
\[
p\equiv-1\pmod u,\qquad p\equiv1\pmod v.
\tag{1}
\]
Take such primes sufficiently large that
\[
i=(p+1)/u,\quad j=(p-1)/v,\qquad 2\le i<j<p-j<p-i\le p-2.
\tag{2}
\]
Let \(N=\sum_{q\le p}\varphi(q)\), and let \(E_1,\ldots,E_{p-2}\) be FD-320's complete directed denominator-\(p\) excursions of the genuine order-\(p\) Farey word. Partition them into the following five nonempty consecutive pieces:
\[
A=E_1\cdots E_{i-1},\quad B=E_i\cdots E_{j-1},\quad
C=E_j\cdots E_{p-j-1},\quad
D=E_{p-j}\cdots E_{p-i-1},\quad R=E_{p-i}\cdots E_{p-2}.
\tag{3}
\]
Farey reflection gives block gap counts \((a,b,h,b,a)\), with \(2a+2b+h=N-2\). Preserve the first and last Farey gaps and concatenate the *same* complete labeled directed-gap words in the orders
\[
\boxed{\sigma=BACRD,\qquad \tau=DACRB.}
\tag{4}
\]
Both reassemblies preserve the complete directed-edge/gap inventories and the endpoints \(0,1\); both are reflection symmetric. Each has **exactly six** noninteger inherited Hall--Shiu indices at the **identical** ordered ranks
\[
\boxed{\mathbf r=(1,\ 1+b,\ 1+a+b,\ N-1-a-b,\ N-1-b,\ N-1).}
\tag{5}
\]
At those ranks their exact index values satisfy
\[
\boxed{p(\boldsymbol\nu^\sigma-\boldsymbol\nu^\tau)
=(-1,1,0,0,1,-1),\qquad
\|\boldsymbol\nu^\sigma-\boldsymbol\nu^\tau\|_\infty=1/p.}
\tag{6}
\]
Nevertheless, for FD-320's excursion transport \(T_p(\omega)\) and the quadratic rank-grid energy
\(E_p^\omega=\sum_{k=1}^{N-1}(x_k^\omega-k/N)^2\),
\[
\boxed{\lim_p(E_p^\sigma-E_p^\tau)
=\lim_p(T_p(\sigma)-T_p(\tau))
=\frac6{\pi^2}d^2(2-\alpha-\beta)>0,}
\tag{7}
\]
where all limits follow (1). More strongly,
\[
\boxed{\lim_p\|D^\sigma-D^\tau\|_2^2
=\frac6{\pi^2}d^3>0,\qquad
\lim_p(\widehat D^\sigma_2-\widehat D^\tau_2)
=\frac{\sqrt6\,d}{\pi^2}(1-\cos(2\pi d))>0.}
\tag{8}
\]
Here \(D^\omega=(x_k^\omega-k/N)_{1\le k<N}\) and
\(\widehat D^\omega_m=\sqrt{2/N}\sum_{k=1}^{N-1}D^\omega_k\sin(\pi mk/N)\). Odd sine modes of either reflected reassembly vanish **exactly**. Thus (8) distinguishes their reflection-allowed spectrum at fixed frequency, not only their total energy.

## 2. All six index values and ranks are exact

Let \(I(t)\) be the representative in \(\{1,\ldots,p-1\}\) of \(t^{-1}\bmod p\). From (1)--(2),
\[
I(1)=1,\quad I(i)=u,\quad I(j)=p-v,\quad
I(p-j)=v,\quad I(p-i)=p-u,\quad I(p-1)=p-1.
\tag{9}
\]
FD-320's inherited seam identity, including its left/right sentinels, is \(p(\nu_{s,t}-1)=I(s+1)-I(t)\) when a preceding excursion label \(s\) is followed by label \(t\). Within any original block the index remains the original integer. Evaluating only the six joins in (4) gives the **complete** integer-numerator signatures
\[
\begin{aligned}
p(\boldsymbol\nu^\sigma-\mathbf 1)
 &= (1-u,\ p-v-1,\ u+v-p,\ u+v-p,\ p-v-1,\ 1-u),\\
p(\boldsymbol\nu^\tau-\mathbf 1)
 &= (1-v,\ p-u-1,\ u+v-p,\ u+v-p,\ p-u-1,\ 1-v).
\end{aligned}
\tag{10}
\]
All displayed numerators are nonzero for sufficiently large \(p\). Their difference proves (6) because \(u-v=1\). In both words the block lengths are \((b,a,h,a,b)\), so summing gap counts between their joins, including the fixed first outer gap, proves (5). Reflection maps \(A\leftrightarrow R\), \(B\leftrightarrow D\), \(C\leftrightarrow C\), and reversal of each word (4) back to itself. Consequently the reconstructed rational grids are individually reflection symmetric, giving exact cancellation of odd Dirichlet sine modes.

FD-331 already proves that, at fixed defect ranks, errors *strictly* smaller than \(1/p\) must vanish identically, because each valid index lies in \(1+p^{-1}\mathbb Z\). The distinct words (4) attain the **least possible nonzero lattice error** on an infinite set of primes. This does not assert that six defects is the smallest defect count at which such an example exists.

## 3. Finite transport identities and unconditional limit

Let the original normalized gap-count minus geometric-width imbalances be
\[
x=\frac aN-\frac{i-1}{p},\qquad
y=\frac bN-\frac{j-i}{p},\qquad
z=\frac hN-\frac{p-2j}{p}.
\tag{11}
\]
They satisfy the exact conservation law
\[
2x+2y+z=\frac2p-\frac2N.
\tag{12}
\]
FD-320 gives \(D^\omega=P_\omega D+v^\omega\), where \(D\) is the genuine Farey discrepancy and \(P_\omega\) permutes its coordinates. In the common output block slots of lengths \((b,a,h,a,b)\), the **exact constant transport shifts** for the two orders are
\[
v^\sigma=(x,-y,0,y,-x),\qquad
v^\tau=(x+y+z,-y,0,y,-x-y-z).
\tag{13}
\]
The tuples mean a constant value repeated on each block's full collection of rank positions. Hence
\[
\begin{aligned}
T_p(\sigma)&=2b x^2+2a y^2,\\
T_p(\tau)&=2b(x+y+z)^2+2a y^2,\\
T_p(\sigma)-T_p(\tau)&=2b\,[x^2-(x+y+z)^2],\\
\|v^\sigma-v^\tau\|_2^2&=2b(y+z)^2.
\end{aligned}
\tag{14}
\]
In particular \(v^\sigma-v^\tau\) is exactly \(-(y+z)\) on the first \(b\) excursion ranks, \(+(y+z)\) on the last \(b\) ranks, and zero elsewhere; it is not estimated by counting the six seams.

Let \(\rho_p(1/q)\) count positive genuine Farey fractions at most \(1/q\). Because \(i/p\) is the immediate successor of \(1/u\) and \(j/p\) the immediate predecessor of \(1/v\), there are exact counts
\[
a=\rho_p(1/u),\qquad b=\rho_p(1/v)-\rho_p(1/u)-2.
\tag{15}
\]
The fixed-rational rank estimate \(\rho_p(1/q)=N/q+o_q(p)\) is derived in FD-330 from Möbius inversion and the prime number theorem (no RH); also \(N/p^2\to3/\pi^2\). Thus
\[
\frac aN=\alpha+o(p^{-1}),\quad \frac bN=d+o(p^{-1}),\quad
px\to1-\alpha,\quad py\to\alpha+\beta,\quad
p(y+z)\to-d,\quad p(x+y+z)\to1-\beta.
\tag{16}
\]
Substituting (16) into (14) proves the first transport limit in (7), with the strictly positive constant
\[
\frac6{\pi^2}d[(1-\alpha)^2-(1-\beta)^2]
=\frac6{\pi^2}d^2(2-\alpha-\beta).
\tag{17}
\]
Both transports remain \(O(1)\). FD-320 proves unconditionally from PNT that \(\|D\|_2^2=E_p=o(1)\), uniformly for this permutation argument. Consequently
\[
|E_p^\omega-T_p(\omega)|
 \le E_p+2\sqrt{E_pT_p(\omega)}=o(1),\qquad
\|D^\sigma-D^\tau-(v^\sigma-v^\tau)\|_2\le2\sqrt{E_p}=o(1).
\tag{18}
\]
This establishes the full-energy limit (7) and the squared-distance limit (8) using (14)--(16).

For the fixed Fourier assertion, the first and last \(b\) rank blocks occupy asymptotically the normalized intervals \((0,d)\) and \((1-d,1)\). Using (14), (16), \(N/p^2\to3/\pi^2\), and a Riemann sum gives for any fixed \(m\)
\[
\lim_p(\widehat D_m^\sigma-\widehat D_m^\tau)
=\frac{\sqrt6\,d}{m\pi^2}
 [1-(-1)^{m+1}]\,[1-\cos(m\pi d)].
\tag{19}
\]
This vanishes for odd \(m\); for \(m=2\) it gives (8). The complete \(L^2\) limiting difference is the antisymmetric step profile
\((\sqrt6\,d/\pi)(\mathbf1_{(0,d)}-\mathbf1_{(1-d,1)})\).
Its Parseval energy is \(6d^3/\pi^2\); thus (8) does not conceal unaccounted high-frequency energy.

## 4. Independent finite and large-order falsification

A separate exact-rational check generated genuine Farey fractions from the recurrence and *copied their actual directed denominator-pair gaps* \(1/(ab)\) through the two orders (4). It separately summed the reconstructed rational grids and their quadratic rank discrepancies, enumerated every noninteger inherited index and its rank, and verified the full directed-edge inventories and endpoint \(1\). For \((v,u,p)=(3,4,19),(3,4,31),(3,4,43),(4,5,29),(4,5,89),(4,5,109)\), all six defect ranks coincided and their index-numerator difference was exactly \((-1,1,0,0,1,-1)\). Each instance checked (14) from independently obtained gap counts.

For \(p=29,u=5,v=4\), \(N=270\), \((a,b,h)=(54,11,138)\), and the common ranks are \((1,12,66,204,258,269)\). The exact numerator tuples from the actual joined denominator words are \((-4,24,-20,-20,24,-4)\) and \((-3,23,-20,-20,23,-3)\). Independent exact energies yield
\[
T_{29}(\sigma)-T_{29}(\tau)=-4763/30654450,\qquad
E_{29}^\sigma-E_{29}^\tau
=472462358671/759865469863500.
\tag{20}
\]
The finite transport difference is not asserted positive; the theorem is asymptotic. A separate Möbius-inversion/totient computation at \(p=229,809,1009,2089,10009\) checked (15), the exact two-block transport formula, and the approach to its limit without reconstructing all \(O(p^2)\) Farey gaps. These checks test arithmetic and edge bookkeeping, not the PNT theorem.

## 5. Prior art, identification boundary, and consequence

The Hall--Shiu Farey index, modular-inverse denominator-neighbor coding, fixed-rational Farey-rank asymptotics, and prime number theorem are classical. See Hall and Shiu, *The index of a Farey sequence*, Michigan Math. J. **51** (2003), 209--223, DOI 10.1307/mmj/1049832901. Block permutations and breakpoint signatures are standard combinatorics; García, *A General Lower Bound for Average Local Discrepancy and an Application to the Farey Sequence*, *Mathematics* **14** (2026), 2543, DOI 10.3390/math14142543, treats a different average-local gap-permutation statistic. FD-319 already shows vanishing *absolute* index defects can carry a fixed even mode, FD-320 gives the exact all-excursion transport spectrum, FD-330 gives macroscopic rank-only ambiguity, and FD-331 provides exact joint-signature inversion. The distinct line-local contribution here is **the least possible nonzero index-value error at perfectly matched ranks while macroscopic scalar and even-mode separation both persist**. A targeted literature check did not find this specialized construction; no general priority claim is made.

These reassemblies are labeled-edge controls only. At the six defective seams, inherited denominator labels need not be actual reduced denominators of the reconstructed rational vertices; the strings are not competing genuine Farey sequences. Knowing the prime and the exact values/ranks still determines each word by FD-331. This result rules out a *prime-uniform* energy/spectral continuity modulus at the lattice scale \(1/p\) even with same edge inventory and reflection, not exact identifiability and not any RH-critical bound. No improvement to Franel--Landau or the Riemann hypothesis follows.
