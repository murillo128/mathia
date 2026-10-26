# XF-209 — covered edge spikes have vanishing fixed-time total variation

**Status:** `EXACT-DERIVED` + `MATCHED-CONTROL` + `STRUCTURAL/DYNAMIC`.

The instantaneous counterexample in XF-208 does not persist as an
integrated loss in that same family. There is an absolute time
\(T_*>0\), independent of the period and initial small gap, on which
both smooth-taper families of XF-208 have

\[
\boxed{\int_0^{T_*}|\mathcal K_{a^{(M)}}'(t)|\,dt=O_A(M^{-3}).}
\tag{1}
\]

In particular their negative variation and their net change vanish,
even though the initial derivatives respectively tend to \(-\infty\)
and \(-50/441\). The estimate follows the **complete periodic heat
flow**, with all periodic images retained. It includes the production
that develops in triples initially having equal gaps.

This is a forward-time, family-specific result. It neither repairs the
false pointwise estimate excluded by XF-208 nor proves a time-integrated
localization theorem for arbitrary Xi configurations. It supplies a
uniform real-simple interval for this control and closes its possible
promotion into a fixed-time adverse-integral example.

The initial gap law matters for **absolute** variation. With the same
profiles but an unrestricted initial gap, Section 5 gives the sharp
threshold \(a_0\log(1/\epsilon)\to0\). Negative variation still vanishes
uniformly in the gap: any surviving initial-time concentration has
positive sign. Thus a missing logarithmic gap bound obstructs absolute
variation control, but does not resurrect an adverse-integral example
within this isolated-defect family.

## 1. Precise control and quantitative estimate

Let \(N=8M\) and use the XF-208 roots
\[
x_{Nm+j}(0)=Nm+b_j,\quad
b_0=0,\quad b_1=\epsilon,\quad b_2=1+\epsilon,\quad
b_j=j\ (3\le j<N).
\tag{2}
\]
Their entire heat flow is
\[
f_t=e^{-t\partial_z^2}\prod_{j=0}^{N-1}
\sin\frac{\pi(z-b_j)}N.
\tag{3}
\]
Write \(g_i=x_{i+1}-x_i\), \(d_j=\log(g_{j+1}/g_j)\), and
\(\mathcal J_j=F(d_j)\), with the exact XF-030 derivative
\[
F'(d)=\phi(e^d),\qquad
\phi(r)=-\frac{(r-1)(r+2)(2r+1)}{(r+1)(r^2+r+1)}.
\tag{4}
\]
For fixed nonnegative weights supported on \(0\le j<3M\), put
\(\mathcal K_a=\sum_j a_j\mathcal J_j\),
\(\alpha=a_0\), and \(\beta=a_1\).

There are absolute \(\epsilon_*,T_*,C>0\) such that for every
\(0<\epsilon\le\epsilon_*\), all sufficiently large \(M\), and
\(0\le T\le T_*\), the roots in (3) remain real and simple and
\[
\boxed{
\int_0^T|\mathcal K_a'(t)|\,dt
\le C\left[
\alpha\log\left(1+\frac{4T}{\epsilon^2}\right)
+\beta\sqrt T
+T\sum_{j=2}^{3M-1}\frac{a_j}{(1+j)^4}
\right].}
\tag{5}
\]
The constants do not depend on \(M,\epsilon,a\). No gap floor uniform
in \(\epsilon\) is assumed at time zero.

## 2. A real-simple interval uniform in the small gap and period

Set \(u_i=i-x_i\), periodically extended with period \(N\). Subtracting
the stationary integer-lattice field gives the absolutely convergent
equation
\[
u_i'=2\sum_{k\ne i}
\frac{u_k-u_i}{(i-k)(i-k-u_i+u_k)}.
\tag{6}
\]
The index sum is over the entire integer line; same-residue images
have zero numerator. It is the difference form of the cotangent
velocity \((2\pi/N)\sum_{k\ne i}\cot(\pi(x_i-x_k)/N)\).
Its off-diagonal derivatives in the finite periodic system are
positive, and every constant \(u_i=c\) is stationary. Equivalently,
at a maximum of \(u\), every term in (6) is nonpositive. Initially
only \(u_1=u_2=1-\epsilon\) are nonzero, so
\[
0\le u_i(t)\le1
\tag{7}
\]
while the roots are ordered. In particular every gap is at most two,
and \(|x_i-x_k|\ge |i-k|-1\).

Bootstrap that all gaps other than \(g_0\) and its periodic copies
exceed \(1/2\), and that \(g=g_0\) stays small. Every root outside
the close pair then has uniformly bounded velocity: in the lattice
subtraction formula, the summand is \(O(|i-k|^{-2})\). The adjacent
denominator is bounded below by \(1/2\); for \(|i-k|\ge2\), (7)
gives the required lower bound. The close pair itself has
\[
x_0'=-2/g+O(1),\qquad x_1'=2/g+O(1).
\tag{8}
\]
The remainders and their difference quotient are uniformly bounded.
Indeed the exterior roots stay at least \(1/2\) from the pair, and
the derivative of their reciprocal field is bounded by a convergent
inverse-square sum. The constant part of that field is bounded by
subtracting the integer lattice and pairing the distant terms.
These bounds include all images and are independent of \(N\).

More exactly, with \(q=g^2\),
\[
q'=8-4qS,\qquad
S=\sum_{z\notin\{x_0,x_1\}}
\frac1{(x_0-z)(x_1-z)},\qquad 0\le S\le C.
\tag{9}
\]
Every exterior root is outside the interval between the pair, which
gives the sign. Choose absolute \(\epsilon_*\) and \(T_*\) small
enough that \(C(\epsilon_*^2+8T_*)\) is small. Then
\[
\epsilon^2+4t\le g(t)^2\le\epsilon^2+8t
\quad(0\le t\le T_*).
\tag{10}
\]
The center of the pair moves by \(O(t)\), and its two roots move
by at most \(O(t+\sqrt t)\) from their initial positions. All other
roots move by \(O(t)\). Since every other initial gap is at least
one, reducing \(T_*\) makes all those gaps at least \(3/4\).
This closes the bootstrap with strict margin, uniformly in
\(M,\epsilon\).

For each positive \(\epsilon\), the finite periodic ODE therefore
continues through this interval without collision. It agrees with
the simple zeros of (3) by implicit differentiation and uniqueness.
Multiplying the finite Fourier sum (3) by \(e^{\pi iz}\) gives a
degree-\(N\) polynomial in \(e^{2\pi iz/N}\), with nonzero extreme
coefficients at every finite time. The \(N\) continued real zeros
per period account for every zero. Thus this is a complete real-entire
heat flow on a common interval, not a finite-root approximation.

## 3. A uniform spatial tail for the moving defect

A bounded velocity alone would allow a sum over \(M\) triples to
lose uniformity. We need decay with distance from the defect.

Let \(\rho_i\) be circular index distance from \(i\) to \(3/2\),
choose a fixed large \(R\), say \(R=64\), and set
\[
b_i^*=2(1+\rho_i/R)^{-2}.
\tag{11}
\]
This profile dominates the initial \(u\), has adjacent difference
at most \(4/R\), and obeys the uniform convolution estimate
\[
\sum_{k\ne i}\frac{b_k^*}{(i-k)^2}\le C_R b_i^*.
\tag{12}
\]
For completeness, periodize the inverse-square kernel. For distinct
residues it is bounded by a constant times the inverse square of
their circular distance; its row sum is bounded independently of
\(N\). If \(\rho_i=r\) is large, split residues according as
\(\rho_k\ge r/2\) or \(\rho_k<r/2\). In the first set,
\(b_k^*\le4b_i^*\), so use the row sum. In the second, circular
distance from \(i\) to \(k\) is at least \(r/2\); use
\(\sum_{k\bmod N}b_k^*\le C_R\). Both contributions are
\(O_R((1+r)^{-2})\). Bounded \(r\) follows from the row sum, and
the same-residue images contribute only \(O(N^{-2})b_i^*\).
This proves (12) with no limit in \(N\).

Put \(U_i(t)=e^{Lt}b_i^*\). While \(e^{Lt}\le2\), its adjacent
differences are less than \(1/2\), so the associated roots
\(i-U_i\) are strictly ordered. The right side of (6) evaluated
at \(U\) is at most
\[
4e^{Lt}\sum_{k\ne i}\frac{b_k^*}{(i-k)^2}
\le4C_R e^{Lt}b_i^*.
\tag{13}
\]
Here terms with negative numerator can be discarded for the upper
bound. Take \(L\ge4C_R\) and reduce \(T_*\) so that
\(e^{LT_*}\le2\). The cooperative comparison principle, or its
first-contact proof applied to the finite periodic ODE, now gives
\[
0\le u_i(t)\le U_i(t)\le2b_i^*.
\tag{14}
\]
At first contact, the self coordinate agrees and all other coordinates
of \(u\) are below those of \(U\); the positive off-diagonal
derivatives of (6) give the comparison. A strict supersolution
followed by a limit removes equality at contact. No coefficient
bound involving the small actual gap is required for this argument.

For \(i\not\equiv0,1\pmod N\), the separation proved in Section 2
and the lattice-subtracted velocity formula imply
\[
|x_i'|\le C\sum_{k\ne i}\frac{u_i+u_k}{(i-k)^2}
\le C b_i^*.
\tag{15}
\]
In the taper range \(2\le i\le3M+1\), its distance from the next
periodic defect is comparable to its distance from the first, and
\(b_i^*\le C(1+i)^{-2}\). Consequently, for every \(2\le j<3M\),
\[
|d_j|+|d_j'|\le C(1+j)^{-2},\qquad
|\mathcal J_j'|\le C(1+j)^{-4}.
\tag{16}
\]
The first bound uses \(g_i=1+u_i-u_{i+1}\), the ordinary-gap floor,
and (15). The second uses \(\phi(1)=0\) and bounded derivative of
\(d\mapsto\phi(e^d)\) on the compact contrast interval imposed by
\(3/4\le g_i\le2\). It includes every formerly equal-gap triple.

## 4. Integrating the two singular triples

The rational function in (4) has \(|\phi(r)|\le2\) for \(r>0\).
For example, its numerator without the minus sign is
\(2r^3+3r^2-3r-2\), while twice its denominator minus that numerator
is \(r^2+7r+4>0\); reciprocal symmetry handles \(r<1\).
Equations (8)--(10) therefore give
\[
|\mathcal J_0'|\le C/g^2,\qquad
|\mathcal J_1'|\le C(1+1/g).
\tag{17}
\]
Only \(\mathcal J_0\) contains the small internal gap on the
nonnegative-index side; \(\mathcal J_1\) feels the singular velocity
of the nearby root. All negative-index weights vanish.

The precise integrable bounds are
\[
\int_0^T\frac{dt}{g(t)^2}
\le\frac14\log(1+4T/\epsilon^2),\qquad
\int_0^T\frac{dt}{g(t)}
\le\frac{\sqrt{\epsilon^2+4T}-\epsilon}{2}
\le\sqrt T.
\tag{18}
\]
Integrate \(|\mathcal K_a'|\le\sum_j a_j|\mathcal J_j'|\), using
(16)--(18) and \(T_*\le1\), to obtain (5). In particular there is
no cancellation of positive and negative time contributions hidden
in this estimate.

For either fixed smooth profile of XF-208, write
\(a_j=A((j+1)/M)\). Flatness at zero implies
\(A(s)\le C_A s^4\) on \([0,3]\), and hence
\[
\sum_{j=2}^{3M-1}\frac{a_j}{(1+j)^4}\le C_A M^{-3}.
\tag{19}
\]
Their two endpoint laws are indexed by \(p\in\{1,2\}\):
\[
\alpha=e^{-M^p},\qquad \beta=e^{-M^p/2^p},\qquad
\epsilon=\frac{42}{5}\frac\alpha\beta.
\tag{20}
\]
Thus \(\alpha\log(1+4T_*/\epsilon^2)=O(M^p e^{-M^p})\) and
\(\beta\sqrt{T_*}=O(e^{-M^p/2^p})\). Substitution into (5)
proves (1). This rate is an upper bound, not a sharp asymptotic.

## 5. Sharp gap-depth boundary and the sign of concentration

Keep the roots (2) and either profile from XF-208, but now allow
**any** sequence \(0<\epsilon_M\le\epsilon_*\), independently of
\(\alpha_M=a_0\) and \(\beta_M=a_1\). Only the initial-gap choice in
(20) is released. The uniform continuation and spatial-tail estimates
in Sections 2--3 still apply. Fix \(0<T\le T_*\), independently of
\(M\), and define
\[
V_M^\pm(T)=\int_0^T(\pm\mathcal K_a'(t))_+\,dt,
\qquad V_M(T)=V_M^+(T)+V_M^-(T).
\]
Then, uniformly in the initial gap,
\[
\boxed{\begin{aligned}
V_M^-(T)&=O_A(M^{-3}),\\
V_M(T)&=2\alpha_M\log(1/\epsilon_M)+O_{A,T}(M^{-3}),\\
\mathcal K_a(T)-\mathcal K_a(0)
&=2\alpha_M\log(1/\epsilon_M)+O_{A,T}(M^{-3}).
\end{aligned}}
\tag{21}
\]
In particular,
\[
V_M(T)\longrightarrow0
\quad\Longleftrightarrow\quad
\alpha_M\log(1/\epsilon_M)\longrightarrow0.
\tag{22}
\]
This characterizes the initial-gap restriction behind (1); it is not
a new positivity theorem for arbitrary configurations.

To prove the sign and the matching lower bound, retain the singular
logarithm rather than estimate the whole first triple absolutely. Put
\(g=g_0\), \(h=g_1\), and \(q=g^2\). The exact XF-030 formula gives
\[
\mathcal J_0=\log q+R(g,h),\qquad
R(g,h)=2\log h+2\log(g+h)
-3\log\!\left[\frac23(g^2+gh+h^2)\right].
\tag{23}
\]
Here \(R\) extends smoothly to \(g=0\) on the closed range
\(0\le g\le g_*\), \(3/4\le h\le2\) supplied by Section 2,
where \(g_*\) is an absolute small constant. Its first derivatives
are uniformly bounded. For example,
\[
R_g=\frac2{g+h}-\frac{3(2g+h)}{g^2+gh+h^2},\qquad
R_h=\frac2h+\frac2{g+h}-\frac{3(g+2h)}{g^2+gh+h^2}.
\]
Equations (8)--(10) imply
\(|g'|+|h'|\le C(1+1/g)\) and \(4\le q'\le8\).
Consequently (18), with \(T_*\le1\), yields
\(\int_0^T|\partial_tR(g,h)|\,dt\le C\sqrt T\).
Combining this with (16)--(18) gives the exact decomposition
\[
\mathcal K_a'=\alpha\frac{q'}q+r_M,
\qquad
\int_0^T|r_M(t)|\,dt
\le C\left[(\alpha+\beta)\sqrt T
+T\sum_{j=2}^{3M-1}\frac{a_j}{(1+j)^4}\right].
\tag{24}
\]
The first term is nonnegative. Therefore negative variation is at
most the right side of (24), while both total variation and net change
differ from \(\alpha\log(q(T)/\epsilon^2)\) by at most that same
quantity. For fixed positive \(T\), (10) bounds \(q(T)\) above and
below by positive constants independent of \(M,\epsilon\).
Using (19), \(\alpha=e^{-M^p}\), and
\(\beta=e^{-M^p/2^p}\) proves (21)--(22). The constants in
\(O_{A,T}\) may grow as \(T\downarrow0\); a shrinking observation
interval is not covered by (21).

There is a precise concentration interpretation. For any finite
\(L\ge0\), if
\(2\alpha_M\log(1/\epsilon_M)\to L\), then on the **closed**
interval \([0,T]\), as finite signed measures,
\[
\boxed{\mathcal K_a'(t)\,dt\ \rightharpoonup\ L\delta_0.}
\tag{25}
\]
Indeed the nonnegative measure \(\alpha_M q'/q\,dt\) has total
mass tending to \(L\). For every fixed \(0<\delta<T\), its mass on
\([\delta,T]\) is
\(\alpha_M\log(q(T)/q(\delta))=O_{\delta,T}(\alpha_M)\to0\).
Testing against a continuous function and then taking \(\delta\downarrow0\)
proves convergence to \(L\delta_0\); (24) removes the remainder in
total variation. For each \(L>0\), the explicit admissible choice
\[
\epsilon_M=\exp[-L/(2\alpha_M)]
\tag{26}
\]
realizes this limit for all sufficiently large \(M\). These are genuine
positive gaps, with the same bounded lattice displacement, upper gaps,
taper smoothness, and positive core coverage as before. No numerical
representation of this doubly small gap is needed for the proof.

Thus taper smoothness and bounded counting discrepancy alone do not
make the derivative uniformly integrable at the initial time. The
missing input for absolute variation is logarithmic gap-depth control.
The surviving mass in (25) is **positive** opening-pair production;
it does not falsify a one-sided lower bound for the integrated
derivative. Even gaps much smaller than (26) cannot make the negative
variation exceed (21). The tuned gaps (20) have
\(\alpha_M\log(1/\epsilon_M)=O(M^p e^{-M^p})\), so (1) remains
unchanged. At a collision itself \(\epsilon=0\), the logarithmic
observable is undefined; no ordered-zero ODE is continued through it.

## 6. Prior art, stress tests, and remaining boundary

The reciprocal zero ODE and square-root opening of a pair are classical;
see Tao's [heat-flow exposition](https://terrytao.wordpress.com/2017/10/17/heat-flow-and-zeroes-of-polynomials/)
(with the time sign reversed here), and the cotangent partial fraction
[DLMF 4.22.3](https://dlmf.nist.gov/4.22.E3). Order comparison for a
cooperative ODE and convolution stability of an inverse-square tail
are also classical mechanisms. The log/Riesz-gas contraction literature,
including [Guillin--Le Bris--Monmarche](https://doi.org/10.5802/jep.235),
provides neighboring theory; no stochastic or mean-field theorem from
it is being substituted for the periodic estimates proved above.

[Rodgers--Tao, Section 9, Proposition 28](https://arxiv.org/pdf/1801.05914v5)
uses selected separated boundaries for localized-energy propagation.
That different energy and source-dependent boundary argument does not
already supply (5). Locally, XF-040 and XF-041 establish periodic gap
damping, including a nonlinear variance estimate without an initial
gap floor. A global variance estimate does not control this singular,
spatially tapered discriminant's total time variation. The additional
content here is the uniform isolated-pair continuation and spatial-tail
estimate that make (5) quantitative for the XF-208 edge family.
No literature-wide novelty claim is made.

The logarithmic singularity of a discriminant and its relation to
logarithmic-particle energy are classical, also explicit in Tao's
exposition above. Initial-layer concentration of a nonnegative measure
is an elementary compactness mechanism. Section 5 applies these facts
to the same complete periodic control, using the uniform continuation
and tail bounds to isolate the entire nonvanishing mass. Its additional
content is the sharp weighted logarithmic threshold and the separation
of positive concentration from vanishing adverse variation, not a new
general logarithmic-energy law.

The proof was checked at the potentially nonuniform steps: comparison
uses an ordered supersolution rather than the singular actual
coefficients; the gap opening is uniform in the period; distant
triples are bounded after evolution, not discarded because they were
initially at equilibrium; and integration controls absolute variation.
Exact rational checks verify the coefficients and bounds used for
\(\phi\). Finite convolution checks are only diagnostics; the uniform
convolution proof is (12). No numerical trajectory or Lean proof is
being asserted as evidence.

The direction of time is essential. The result concerns increasing
\(t\) in \(\partial_t f=-\partial_z^2 f\), where the close real
pair opens. It supplies no fixed interval towards decreasing \(t\),
where the pair can collide. In physical spacing \(h\), rescaling
the roots by \(h\) rescales this time interval to \(h^2T_*\);
it is not automatically a fixed Xi-height-independent time gain.

The isolated defect, bounded displacement from a lattice, and lack of
external replenishment are load-bearing. Many interacting defects,
source-driven boundary flux, or uniformly covered finite-gap interior
geometry are outside (5). These controls do not satisfy the full Xi
source law, and no bound on the de Bruijn--Newman constant follows.
The overlap clue still needs an estimate for its actual source class.
The XF-208 tuned-gap sequences have vanishing absolute variation, and
the same isolated-defect family has vanishing negative variation for
every positive initial gap. Without the threshold (22), its absolute
variation can survive or diverge through positive production alone.
