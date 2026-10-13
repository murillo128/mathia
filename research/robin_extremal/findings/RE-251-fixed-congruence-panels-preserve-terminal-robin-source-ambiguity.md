# RE-251 — Fixed congruence panels preserve terminal Robin-source ambiguity

**Status:** EXACT-DERIVED + CONGRUENCE-PRESERVING INTEGER TRANSPORT + SHARP-MATCHED-SOURCE-OBSTRUCTION + PRIOR-ART-BOUNDED; independent adversarial review pending.

**Parent findings:** RE-247, RE-249, RE-250; ordinary-divisor realization boundary RE-057.

RE-250 shows a one-unit discontinuity for integer-valued generalized-prime labels: requiring changes of consecutive gaps below one unit freezes the source, yet allowing one unit permits the full terminal ambiguity. The question here is whether requiring *every transported label to preserve its arithmetic residue* and imposing an all-height quantitative PNT estimate separately in each residue class restores rigidity. For any fixed modulus it does not. These synthetic labels may be composite and are not ordinary primes.

## 1. Fixed-modulus theorem

Fix an integer \(L\ge2\), write \(m=\varphi(L)\), and choose a periodic enumeration \(c_j\) of all reduced classes modulo \(L\), each appearing exactly once per period \(m\). Fix \(b>0\), \(0<\alpha<3/4\), \(p\to\infty\), \(U=U(p)\) with \(U/p\to\infty\), and put
\[
a=e^{-2},\quad T=aU,\quad
V(t)=\frac{(\log t)^{3/5}}{(\log\log t)^{1/5}},\quad
E(t)=t e^{-bV(t)},\quad E_U=E(U),
\]
\[
B_{p,b,U}=\frac{\sqrt p\log p}{\log U}e^{-bV(U)},\qquad
\eta_{\mathrm{crit}}=(\log U)e^{-bV(U)}.
\]
For an integer-label generalized-prime source \(Q=(q_j)\), let
\[
\vartheta_{Q,c}(t)=
\sum_{\substack{q_j\le t\\q_j\equiv c\pmod L}}\log q_j,
\qquad
\vartheta_Q=\sum_{c\in(\mathbb Z/L\mathbb Z)^\times}\vartheta_{Q,c}.
\]

**Theorem.** There exist one fixed strictly increasing sequence \(Q_L=(q_j)\) of integers \(>1\), all coprime to \(L\), with \(q_j\equiv c_j\pmod L\), and one fixed \(t_0=t_0(L,b)\), such that
\[
q_{j+1}-q_j=\log q_{j+1}+O_L(1),\qquad
\vartheta_{Q_L,c}(t)=\frac{t}{m}+O_L(\log t),
\]
and \(|\vartheta_{Q_L,c}(t)-t/m|\le E(t)/(4m)\) for \(t\ge t_0\).

An *admissible transport* \(R=(r_j)\) is a strictly increasing indexed sequence of integer labels \(>1\) satisfying all of the following: \(r_j\equiv q_j\pmod L\); \(r_j=q_j\) for original labels outside \((T,U)\), with all interior labels remaining inside \((T,U)\); the **same all-height classwise unit envelope**
\[
\left|\vartheta_{R,c}(t)-\frac t m\right|\le\frac{E(t)}m
\quad(t\ge t_0,\;c\in(\mathbb Z/L\mathbb Z)^\times);
\]
and, for every adjacent pair, including both shell-straddling pairs,
\[
|(r_{j+1}-r_j)-(q_{j+1}-q_j)|\le\eta .
\]

Use RE-247's actual normalized terminal observable
\[
h(t)=\frac{-\log(1-t^{-1})}{\log t},\quad
Z_{p,U}=\sqrt p\log p\int_{p+p^\alpha}^U\sqrt t\,(-h'(t))\,dt
=2+o(1),
\]
\[
\mathcal A_{p,U}(R)=\frac{\sqrt p\log p}{Z_{p,U}}
\int_{p+p^\alpha}^U(t-\vartheta_R(t))(-h'(t))\,dt.
\]
Let \(\Delta^{(L)}_{p,b,U}(\eta)\) be the supremum of
\(|\mathcal A_{p,U}(R^1)-\mathcal A_{p,U}(R^2)|\) over admissible transports of **this same** \(Q_L\). Then
\[
\boxed{\Delta^{(L)}_{p,b,U}(\eta)=0\quad(0\le\eta<L),}
\]
\[
\boxed{\Delta^{(L)}_{p,b,U}(\eta)=(2+o(1))B_{p,b,U}
\quad(\eta\ge L).}
\]
The second estimate is uniform over arbitrary \(\eta=\eta_U\ge L\), as a single constructed pair has gap distortion at most \(L\). For a fixed finite panel of moduli, take \(L\) to be their least common multiple: residues are preserved simultaneously, and summation over classes above a fixed divisor \(d\mid L\) gives the bound \(E(t)/\varphi(d)\) in every reduced class modulo \(d\). Here \(L\) must stay fixed as \(U\to\infty\).

## 2. A single fixed source balanced in every reduced class

Let \(x_1=2\) and \(x_{j+1}-\log x_{j+1}=x_j\), the strictly increasing real baseline of RE-247, so \(x_{j+1}-x_j=\log x_{j+1}\) and \(\vartheta_X(t)=t+O(\log t)\). For all sufficiently large \(j\), choose \(q_j\) as the integer closest to \(x_j\) in residue class \(c_j\pmod L\). Thus \(q_j=x_j+O(L)\), and eventually \(q_{j+1}>q_j\) and \(q_{j+1}-q_j=\log q_{j+1}+O_L(1)\). Complete the finite initial part with \(q_j=Lj+c_j\) until a large fixed junction index \(J(L)\); since \(x_J/J\to\infty\), choose the junction to keep the whole sequence strictly increasing.

The change in each logarithmic weight from moving \(x_j\) by \(O(L)\) is \(O_L(1/x_j)\). Since the original labels have gaps comparable to \(\log x_j\), their reciprocal sum up to \(t\) is \(O(\log\log t)\); at most \(O_L(1)\) labels near any sufficiently large threshold change sides under the bounded rounding, contributing \(O_L(\log t)\). The finitely many initial differences contribute a constant. Hence \(\vartheta_{Q_L}(t)=t+O_L(\log t)\).

The bounded partial sums of the periodic indicator \(1_{\{c_j=c\}}-1/m\), combined with summation by parts against the increasing \(\log q_j\), give
\(\vartheta_{Q_L,c}(t)-\vartheta_{Q_L}(t)/m=O_L(\log t)\).
Therefore \(\vartheta_{Q_L,c}(t)=t/m+O_L(\log t)\). As \(E(t)/\log t\to\infty\), a single sufficiently large \(t_0(L,b)\) supplies the asserted quarter-envelope for every reduced class.

## 3. Exact rigidity below the lattice spacing

Set \(d_j=r_j-q_j\in L\mathbb Z\). Every difference of consecutive gaps is \(d_{j+1}-d_j\in L\mathbb Z\). If \(\eta<L\), each such difference must vanish. The common displacement is zero because the exterior labels are fixed. Thus \(R=Q_L\) exactly, proving the first assertion without any PNT input.

## 4. Matching integer transports above the threshold

Write \(f_M(u)=\min\{u,M(u-a),M(1-u)\}\) for \(a\le u\le1\), and zero outside. This is nonnegative, at most \(u\), globally \(M\)-Lipschitz, and vanishes at both endpoints. Choose
\[
\delta=(\log U)^{-1/2},\quad \lambda=1-\delta,\quad
M=\frac{L}{4\eta_{\rm crit}}\longrightarrow\infty,\quad
s_j=\lambda E_U f_M(q_j/U),
\]
\[
d_j=L\left\lfloor \frac{s_j}{L}+\frac12\right\rfloor,\qquad
r_j^\pm=q_j\pm d_j.
\]
All exterior displacements vanish. For every pair of adjacent baseline labels meeting the shell, including straddling pairs,
\[
|s_{j+1}-s_j|\le\lambda\frac{E_U M}{U}(q_{j+1}-q_j)
=\frac{\lambda L}{4\log U}(q_{j+1}-q_j)
=L/4+o_L(1)<L/3.
\]
Nearest-multiple rounding therefore gives \(|d_{j+1}-d_j|\le L\). The transported gaps remain positive because baseline shell gaps are \(\log U+O_L(1)\to\infty\). Near either endpoint, \(s_j\le [\lambda L/(4\log U)]\min(q_j-T,U-q_j)\); if \(d_j\ne0\), this inequality implies that the rounded displacement is smaller than either boundary distance for all large \(U\). Thus shell membership, strict rank, cardinality, residues, exact exterior agreement and the **global** gap budget \(L\) all hold.

Furthermore
\[
d_j=\lambda E_U f_M(q_j/U)+O(L),\quad
D:=\sup_j|d_j|\le E_U+O(L)=o(U).
\]
For a fixed reduced class \(c\), the cumulative change in its jump weights through a shell index \(j\) is
\[
W_{j,c}^{\pm}=
\sum_{\substack{k\le j,\;c_k=c\\q_k\in(T,U)}}
\log\frac{r_k^\pm}{q_k}
=O_L(E_U/\log U),
\]
because there are \(O_L(U/\log U)\) labels in the shell, all \(q_k\asymp U\). At its transported class-\(c\) jump, with \(d_j^\pm=\pm d_j\), the **exact** staircase identity is
\[
\vartheta_{R^\pm,c}(r_j^\pm)-\frac{r_j^\pm}{m}
=\left(\vartheta_{Q_L,c}(q_j)-\frac{q_j}{m}\right)
+W_{j,c}^{\pm}-\frac{d_j^\pm}{m}.
\]
Two successive class-\(c\) jumps are \(O_L(\log U)\) apart. Since \(f_M(u)\le u\),
\[
d_j\le(1-\delta)E_U(q_j/U)+O(L)
\le(1-\delta)E(q_j)+O(L).
\]
The derivative \(E'(t)=e^{-bV(t)}(1-btV'(t))=o(1)\) on this fixed multiplicative shell implies that replacing \(q_j\) by any \(t\) between the corresponding transported jumps costs only
\(O_L(E_U e^{-bV(U)}+\log U)\). Therefore
\[
\left|\vartheta_{R^\pm,c}(t)-\frac tm\right|
\le \frac{(1-\delta)E(t)}m+
O_L\!\left(\log U+\frac{E_U}{\log U}
                      +E_U e^{-bV(U)}\right)
\le\frac{E(t)}m
\quad(T\le t\le U),
\]
because \(m\) is fixed and \(\delta E_U\) dominates all displayed errors. Below \(T\), the source equals the baseline. Above \(U\), the only residual classwise difference from that baseline is a fixed total changed logarithmic weight \(O_L(E_U/\log U)\), which the increasing \(E(t)/m\) absorbs. Thus both signs obey the same classwise unit bound at **every** \(t\ge t_0\). Summing over the \(m\) classes also yields the aggregate unit envelope \(|\vartheta_{R^\pm}(t)-t|\le E(t)\) needed for the RE-247 upper bound.

## 5. Exact kernel subtraction and sharp constant

For two indexed transports which coincide outside the shell, RE-249's exact positive subtraction identity gives
\[
\mathcal A_{p,U}(R^+)-\mathcal A_{p,U}(R^-)
=\frac{\sqrt p\log p}{Z_{p,U}}
\sum_{q_j\in(T,U)}
\int_{q_j-d_j}^{q_j+d_j}
\left(\frac1{r(r-1)}+\frac{h(U)}r\right)dr.
\]
The integrand is \((1+o(1))/q_j^2\), uniformly over the shell because \(d_j=O(E_U)=o(U)\). The \(O(L)\) positional rounding per index contributes at most
\(O_L(1/(U\log U))=o(e^{-bV(U)}/\log U)\)
to the sum. Baseline gaps \(\log U+O_L(1)\) give positive quadrature
\[
\sum_{q_j\in(T,U)}\frac{E_U f_M(q_j/U)}{q_j^2}
=\frac{e^{-bV(U)}}{\log U}
\left(\int_a^1\frac{f_M(u)}{u^2}\,du+o(1)\right).
\]
The functions \(f_M(u)/u^2\) have uniformly bounded total variation and the mesh is \(O_L(\log U/U)\), so the estimate remains valid as \(M\to\infty\). By dominated convergence the integral tends to \(\int_a^1du/u=2\). Incorporating the two signs, \(\lambda\to1\), and \(Z_{p,U}\to2\) yields
\[
\mathcal A(R^+)-\mathcal A(R^-)
=(2+o(1))B_{p,b,U}.
\]
The aggregate PNT bound embeds the pair in RE-247's admissible comparison class, where \((2+o(1))B_{p,b,U}\) is also the **upper** bound. This proves the theorem for every \(\eta\ge L\) with no dependence of the remainder on \(\eta\).

## 6. Prior-art, falsification boundary and relevance

The lattice-spacing freeze, cyclic residue balancing and rounding are elementary; none is claimed as a new number-theoretic theorem. Compare H. G. Diamond and W.-B. Zhang, *Optimality of Chebyshev bounds for Beurling generalized numbers*, Acta Arith. **160** (2013), 259–275, DOI 10.4064/aa160-3-3: its generalized-integer counting hypotheses and Chebyshev-bound conclusions are **not** the present terminal-kernel and classwise-constrained transport modulus. The mathematical delta beyond RE-250 is that an *arbitrary fixed finite panel* of residue and PNT-in-progression constraints preserves the full synthetic-source ambiguity at gap tolerance \(L\).

Critical checks are the fixed common \(t_0\), periodic class-count discrepancy, all-height classwise envelope including after \(U\), transported logarithmic weights, both straddling gaps, strict shell containment, actual endpoint correction \(h(U)\), and \(Z_{p,U}\to2\). The modulus \(L\) is fixed, not growing. Crucially, composite integer labels are permitted: they do **not** satisfy the prime-atom divisor-sum identity of ordinary primes (cf. RE-057). This result neither restricts actual colossally abundant counterexample profiles nor supplies a new inequality for ordinary \(\sigma(n)\), and does not prove RH.
