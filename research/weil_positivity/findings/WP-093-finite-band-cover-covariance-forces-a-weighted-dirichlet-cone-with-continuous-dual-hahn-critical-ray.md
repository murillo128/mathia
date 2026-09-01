# WP-093 — Finite-band cover covariance forces a weighted Dirichlet cone with a continuous-dual-Hahn critical ray

**Status:** `EXACT-DERIVED + POSITIVE-SURVIVOR + CLASSIFICATION + CLASSICALIZED + MATCHED-CONTROL + NOT-GLOBAL-WEIL`.

`WP-082` leaves open a specific loophole after classifying diagonal homogeneous cover-positive generators: a genuinely **non-diagonal**, matrix-valued positive form might satisfy the exact all-degree cover law without collapsing to the diagonal dyadic/trace mechanisms already rejected. That loophole is nonempty, but it is unexpectedly rigid.

On the canonical cover Hilbert space `ell^2(N_0)`, every Hermitian exact-cover-covariant form of **fixed finite bandwidth** is forced into a three-real-parameter tridiagonal family. Positivity then collapses that family to a two-parameter weighted Dirichlet cone. Its critical ray has an intrinsic factorization `G=T^*T`, exact cover intertwining, and a canonical spectral resolution by continuous dual Hahn polynomials with parameters `(1/2,1/2,1/2)`.

This is a genuine independently positive Mathia-native geometry: neither its sign nor its cover covariance uses zeta, zeros, RH, or a fitted kernel. But aggressive controls also classicalize it. The critical form is the inverse square of the classical discrete Cesaro operator in the precise sense `G^{-1}=C^*C`; its continuous-dual-Hahn Gamma density is not the completed-zeta archimedean factor; and its simplest scalarizations do not recover Mangoldt support. Moreover, the construction exists for every integer cover degree, not only primes.

So the finite-band non-diagonal loophole survives only as a **positive supplier**, not as a global Weil mechanism. Any arithmetic use must introduce a canonical nonseparable prime-sensitive coupling before scalarization while preserving this independent sign theorem; otherwise it is another universal cover-positive geometry with the wrong arithmetic and archimedean outputs.

## 1. Exact all-degree cover covariance

Let

\[
H=\ell^2(\mathbb N_0),
\qquad
W_n e_k=\frac1{\sqrt n}\sum_{r=0}^{n-1}e_{nk+r},
\tag{1}
\]

for every integer `n>=1`. These are the normalized cover/refinement isometries used by the preceding cover calculations. For a Hermitian matrix/form `A` on the finite-support core `c_00`, define the coarse compression

\[
\Phi_n(A)=W_n^*AW_n.
\tag{2}
\]

The exact degree-one scaling law studied here is

\[
\boxed{\Phi_n(A)=nA\qquad\text{for every }n\ge1.}
\tag{3}
\]

Assume additionally that `A` has a fixed finite bandwidth `w`, independent of `n`:

\[
A_{jk}=0\qquad\text{when }|j-k|>w.
\tag{4}
\]

No boundedness of `A` is assumed; all identities below are first identities of quadratic forms/matrices on `c_00`.

## 2. Any fixed finite bandwidth collapses to bandwidth one

Choose any cover degree `n>w`. If `|k-l|>=2`, the two fine blocks

\[
\{nk,\ldots,nk+n-1\},
\qquad
\{nl,\ldots,nl+n-1\}
\]

are separated by more than `w`. Hence every matrix entry contributing to the coarse element `(Phi_n(A))_{kl}` vanishes, so

\[
(\Phi_n(A))_{kl}=0.
\]

By (3),

\[
0=nA_{kl}.
\]

Therefore

\[
\boxed{A_{kl}=0\quad\text{for }|k-l|\ge2.}
\tag{5}
\]

Thus **all fixed finite-band solutions are tridiagonal**, regardless of the original bandwidth. This already removes the possibility that a finite-range higher-neighbour interaction can carry an additional arithmetic scale hidden from the diagonal classification of `WP-082`.

## 3. Cover covariance forces the off-diagonal coefficient to be quadratic

Write

\[
c_m=A_{m-1,m},\qquad m\ge1.
\tag{6}
\]

For adjacent coarse cells `k,k+1`, tridiagonality leaves exactly one fine edge crossing the common boundary: the edge from `n(k+1)-1` to `n(k+1)`. Therefore

\[
(\Phi_n(A))_{k,k+1}
=\frac1n c_{n(k+1)}.
\tag{7}
\]

Equation (3) gives

\[
\frac1n c_{nm}=nc_m,
\qquad n,m\ge1,
\]

hence

\[
\boxed{c_{nm}=n^2c_m.}
\tag{8}
\]

Taking `m=1` and then relabelling yields the exact solution

\[
\boxed{c_m=\gamma m^2,\qquad \gamma\in\mathbb C.}
\tag{9}
\]

The entire non-diagonal part is therefore controlled by one complex number.

## 4. The diagonal is forced as well

Write `d_j=A_{jj}` and `alpha=Re(gamma)`. The diagonal coarse element contains the `n` diagonal entries inside a fine block and the `n-1` internal nearest-neighbour edges:

\[
\frac1n\left[
\sum_{r=0}^{n-1}d_{nk+r}
+2\alpha\sum_{r=0}^{n-2}(nk+r+1)^2
\right]
=nd_k.
\tag{10}
\]

The quadratic sequence

\[
d_j^{(p)}=-2\alpha j^2
\tag{11}
\]

is an exact particular solution. Put

\[
h_j=d_j+2\alpha j^2.
\]

Then the remaining equation is simply

\[
\frac1n\sum_{r=0}^{n-1}h_{nk+r}=nh_k.
\tag{12}
\]

At `k=0`,

\[
\sum_{r=0}^{n-1}h_r=n^2h_0.
\tag{13}
\]

Subtracting the same identity with `n-1` gives

\[
h_{n-1}=(2n-1)h_0.
\]

Thus there is one additional real parameter `b=2h_0` and

\[
\boxed{
 d_j=-2\operatorname{Re}(\gamma)j^2+b\left(j+\frac12\right),
 \qquad b\in\mathbb R.
}
\tag{14}
\]

Combining (5), (9), and (14) gives a complete classification:

\[
\boxed{
\begin{aligned}
A_{jj}&=-2\operatorname{Re}(\gamma)j^2+b(j+\tfrac12),\\
A_{j,j+1}&=\gamma(j+1)^2,\\
A_{j+1,j}&=\overline\gamma(j+1)^2,
\end{aligned}}
\tag{15}
\]

with all other entries zero. The space of Hermitian fixed-finite-band exact-covariant forms is only three-real-dimensional.

## 5. Positivity forces a real negative edge and gives an exact cone

The Hermitian classification still allows complex `gamma`. Positivity removes that freedom.

Take long phase packets supported far out in the lattice, where the leading `j^2` coefficients can be frozen. Their principal local symbol is

\[
-2\operatorname{Re}\gamma
+2\operatorname{Re}(\gamma e^{i\theta}).
\tag{16}
\]

For a positive form this must be nonnegative for every phase `theta`, so in particular its minimum must satisfy

\[
-2\operatorname{Re}\gamma-2|\gamma|\ge0.
\tag{17}
\]

Because `|Re gamma|<=|gamma|`, equality of the two magnitudes is forced and the only possibility is

\[
\boxed{\gamma=-a,\qquad a\ge0.}
\tag{18}
\]

Substitution into (15) gives the exact quadratic-form identity

\[
\boxed{
q_{a,b}(x)
=a\sum_{j\ge0}(j+1)^2|x_{j+1}-x_j|^2
+(b-2a)\sum_{j\ge0}(j+\tfrac12)|x_j|^2.
}
\tag{19}
\]

Therefore `a>=0,b>=2a` is sufficient for positivity.

It is also necessary. If `b-2a<0`, choose a slowly varying packet supported on an interval of length comparable to `N` and centered at scale comparable to `N`. The weighted gradient term in (19) is `O(N)`, while the weighted mass term is `Theta(N^2)`. For large `N` the negative mass dominates. Hence

\[
\boxed{
q_{a,b}\ge0\text{ on }c_{00}
\iff
a\ge0,\ b\ge2a.
}
\tag{20}
\]

This is the exact positive cone inside the complete fixed-finite-band covariant family.

## 6. The critical ray is a canonical weighted Dirichlet energy

At the boundary `b=2a`, normalize `a=1`. The Jacobi matrix is

\[
G_{jj}=2j^2+2j+1,
\qquad
G_{j,j+1}=-(j+1)^2.
\tag{21}
\]

Define the first-order weighted difference operator on `c_00` by

\[
(Tx)_j=(j+1)(x_{j+1}-x_j).
\tag{22}
\]

Then exactly

\[
\boxed{G=T^*T}
\tag{23}
\]

and therefore

\[
\boxed{
\langle x,Gx\rangle
=\sum_{j\ge0}(j+1)^2|x_{j+1}-x_j|^2\ge0.
}
\tag{24}
\]

This is the required kind of sign theorem in the narrow sense relevant to the research mandate: positivity is a geometric/Dirichlet identity and does not assume RH, zeros, or an arithmetic explicit formula.

The form is closable, and its Friedrichs realization gives the canonical positive self-adjoint operator associated with (24).

## 7. The cover law comes from an exact first-order intertwiner

Represent `x` by its Hardy series

\[
f(z)=\sum_{j\ge0}x_jz^j.
\]

Then

\[
(Tf)(z)=(1-z)f'(z)-f(z),
\tag{25}
\]

while (1) becomes

\[
(W_nf)(z)
=\frac1{\sqrt n}\frac{1-z^n}{1-z}f(z^n).
\tag{26}
\]

Differentiating (26) gives the exact identity

\[
\boxed{TW_n=\sqrt n\,V_nT,}
\tag{27}
\]

where

\[
(V_ng)(z)=z^{n-1}g(z^n).
\tag{28}
\]

`V_n` is an isometry onto one residue class. Hence

\[
W_n^*GW_n
=(TW_n)^*(TW_n)
=nT^*V_n^*V_nT
=nG.
\tag{29}
\]

So the covariance is not an accidental coefficient identity: the critical positive form carries a canonical first-order refinement intertwiner.

## 8. Classicalization: the inverse is the Cesaro Gram operator

The equation `Tx=y` is solved exactly by

\[
x_j=-\sum_{k\ge j}\frac{y_k}{k+1}.
\tag{30}
\]

Let `C` be the classical discrete Cesaro operator on `ell^2(N_0)`,

\[
(Cx)_n=\frac1{n+1}\sum_{k=0}^{n}x_k.
\tag{31}
\]

Its adjoint is

\[
(C^*y)_j=\sum_{k\ge j}\frac{y_k}{k+1}.
\tag{32}
\]

Thus, on the natural operator domains,

\[
\boxed{T^{-1}=-C^*,}
\tag{33}
\]

and consequently

\[
\boxed{G^{-1}=C^*C.}
\tag{34}
\]

This is a strong prior-art redirect. The positive geometry is not a newly discovered isolated spectral object: it is canonically tied to the extensively studied Cesaro/Hardy operator. For example, U. Gul, *The Cesaro Operator in ell^2 is Essentially Normal* (arXiv:2311.15245, 2023) places `C` in a classical operator-theoretic literature extending substantially earlier work.

The Mathia-specific novelty claim is therefore only the **classification under the exact cover covariance (3)** and the identification of its critical ray inside the current research architecture, not novelty of the Cesaro operator or of positivity of a Gram form.

## 9. Exact continuous-dual-Hahn spectral resolution

The same critical Jacobi matrix has a second classical identification. Let

\[
q_n(t)=\frac{S_n(t^2;\frac12,\frac12,\frac12)}{(n!)^2},
\tag{35}
\]

where `S_n` is the continuous dual Hahn polynomial. The standard continuous-dual-Hahn recurrence specializes exactly to

\[
\boxed{
(\tfrac14+t^2)q_n(t)
=-n^2q_{n-1}(t)
+(2n^2+2n+1)q_n(t)
-(n+1)^2q_{n+1}(t).
}
\tag{36}
\]

The first two polynomials already expose the shift:

\[
q_0=1,
\qquad
q_1=\frac34-t^2
=1-(\tfrac14+t^2).
\tag{37}
\]

Thus the generalized spectral parameter of `G` is canonically

\[
\boxed{\lambda=\frac14+t^2.}
\tag{38}
\]

The NIST DLMF continuous-dual-Hahn orthogonality formula gives, for the cyclic vector `e_0`, the normalized spectral measure on `t>0`

\[
\boxed{
d\mu(t)
=\frac1{2\pi}
\left|
\frac{\Gamma(\frac12+it)^3}{\Gamma(2it)}
\right|^2dt
=2\pi t\frac{\sinh(\pi t)}{\cosh^2(\pi t)}\,dt.
}
\tag{39}
\]

The normalization follows from the continuous-dual-Hahn norm at `a=b=c=1/2`; equivalently, the density in (39) integrates to one. DLMF §18.25 records both the orthogonality range and the Gamma weight, and §18.26 gives the Wilson/continuous-dual-Hahn standardization and relations:

- https://dlmf.nist.gov/18.25
- https://dlmf.nist.gov/18.26

This spectral identification is exact, not merely asymptotic. Continuous dual Hahn polynomials and their Jacobi operators are classical special-function/representation-theoretic objects; no novelty is claimed for that spectral theory.

## 10. A continuum diagnostic explains the `1/4` threshold but does not arithmeticize it

For large `n`, the recurrence associated with `G` has the continuum principal part

\[
-\frac{d}{dn}\left(n^2\frac{dx}{dn}\right)=\lambda x.
\tag{40}
\]

A power ansatz `x(n)~n^s` gives

\[
\lambda=-s(s+1).
\]

Writing

\[
s=-\frac12+it
\]

produces

\[
\lambda=\frac14+t^2,
\tag{41}
\]

in agreement with the exact special-function resolution. Under the logarithmic coordinate `n=e^u` and the corresponding half-density conjugation, the principal continuum model is the familiar threshold operator `-d^2/du^2+1/4`.

This is only a diagnostic of the geometry's scale behavior. The exact content is already (36)--(39); no arithmetic conclusion follows merely from seeing the critical-looking constant `1/4`.

## 11. Finite-section determinants are explicit but immediately fail the mandate

Let `G_N` be the `N x N` leading principal section, with the terminal Dirichlet edge included in the finite difference factor. The corresponding upper-bidiagonal `T_N` has diagonal entries `-1,-2,...,-N`, so

\[
\det T_N=(-1)^N N!.
\]

Therefore

\[
\boxed{\det G_N=(N!)^2=\Gamma(N+1)^2.}
\tag{42}
\]

This is a useful exact diagnostic and nothing more. The research mandate explicitly rejects a route that merely manufactures another determinant or Gamma expression. In fact, this determinant supplies a matched falsification test: its arithmetic primitive is wrong.

For example, the divisor-Mobius primitive of its logarithm is

\[
R(n)=\sum_{d\mid n}\mu(d)\,2\log((n/d)!).
\tag{43}
\]

There is no prime-power support: `R(n)` is generally nonzero for integers containing several distinct primes, and at `p^k` it is a factorial-scale expression rather than `log p`. Refinement ratios similarly contain cutoff-scale terms. Recovering `log n` or `Lambda(n)` from (42) would therefore require an extra subtraction/regularization not forced by the positive geometry.

## 12. Matched controls aggressively separate the survivor from Weil positivity

The construction passes the **independent positivity** test but fails the arithmetic/global bridge tests in several different ways.

### 12.1 All-integer cover control

Equations (1), (22), and (27) exist for every integer `n>=1`. No step recognizes primes or prime powers. Therefore

\[
\boxed{
\text{exact cover covariance + the Dirichlet sign theorem}
\text{ is arithmetically universal.}
}
\tag{44}
\]

Replacing prime-labelled covers by all composite degrees leaves the positive mechanism unchanged. This is a direct matched control against interpreting the sign theorem itself as Riemann arithmetic.

### 12.2 The simplest scalarization has the wrong finite support

Equation (43) fails to produce the von Mangoldt selector. Other immediate scalarizations of `G_N` inherit the same problem: they are natural functions of a universal integer-cover operator and have no intrinsic prime-power support. `WP-030` showed that Prime Lattice can create `Lambda(n)` by a very different rank/volume degeneracy mechanism; nothing analogous is present in the finite-band cover form alone.

### 12.3 The exact Gamma density is the wrong archimedean Gamma family

The density (39) involves

\[
\left|\frac{\Gamma(\frac12+it)^3}{\Gamma(2it)}\right|^2.
\tag{45}
\]

The completed Riemann zeta function instead carries

\[
\pi^{-s/2}\Gamma(s/2),
\]

which on the critical line uses `Gamma(1/4+it/2)`. These are not the same local factor, nor does (39) automatically generate the pole/global counterterms in the Weil explicit formula. The appearance of a Gamma density and a `1/4+t^2` threshold is therefore structurally suggestive but **not a match to the Riemann archimedean place**.

### 12.4 Classical prior-art control

Continuous dual Hahn polynomials are a standard Wilson-class family. DLMF lists their positive orthogonality on `(0,infinity)` for positive parameters and their Gamma weight. The Cesaro operator is likewise classical. Related special-function representation theory includes continuous dual Hahn systems in `su(1,1)`-type oscillator/Jacobi settings; for example Jafarov--Stoilova--Van der Jeugt, arXiv:1202.3541, uses continuous dual Hahn wave functions in a deformed `su(1,1)` oscillator model.

Thus neither the spectral family nor the positivity theorem should be advertised as new mathematics. The repository-level result is the exact rigidity statement: **the fixed-finite-band all-degree cover-covariant positive cone is forced into this classical weighted-Dirichlet/Cesaro/continuous-dual-Hahn structure**.

## 13. Novelty audit and exact boundary of the claim

A directed prior-art search covered continuous dual Hahn recurrence/orthogonality, Jacobi-operator realizations, Cesaro operators on `ell^2`, weighted discrete differences, Hardy/Cesaro adjoints, and representation-theoretic appearances of continuous dual Hahn polynomials. It found abundant classical machinery for the resulting operator but did not expose the Mathia-specific classification problem (3)--(4).

Accordingly, this finding claims **no new general theorem about continuous dual Hahn polynomials, Cesaro operators, Hardy inequalities, or Jacobi matrices**. Its durable content is the conjunction of:

1. the exact normalized cover isometries already intrinsic to the Mathia cover model;
2. all-degree covariance `W_n^*AW_n=nA`;
3. fixed finite interaction range;
4. exact classification of all Hermitian solutions;
5. exact classification of the positive cone;
6. identification of the critical positive ray with standard classical objects;
7. explicit matched controls showing why that ray is not yet Weil positivity.

A counterexample to any of the classification equations (5), (9), (14), or to the positive cone (20), under the stated hypotheses, falsifies the result. An infinite-range kernel, a degree-dependent bandwidth, a prime-dependent deformation, or a nontrivial global sector transforming with refinement does not falsify it; those lie outside the class being closed.

## Research consequence

The non-diagonal loophole left by `WP-082` is now sharply split into a solved finite-range part and a genuinely harder nonlocal part:

\[
\boxed{
\begin{array}{c}
\text{fixed finite range}\\
+\ W_n^*AW_n=nA\\
+\ A\succeq0
\end{array}
\Longrightarrow
\begin{array}{c}
\text{weighted Dirichlet cone}\\
\text{with critical }G=T^*T\\
\text{classical Cesaro / continuous dual Hahn}
\end{array}
}
\tag{46}
\]

This is a **real positive survivor** because its sign comes from geometry rather than from RH or inserted zero data. It is nevertheless **not a global Weil-type positivity statement**: it is universal over integer degrees, does not intrinsically produce `Lambda`, and has the wrong exact Gamma family.

The next admissible route cannot simply add more finite-band matrix entries. It must introduce a canonical **infinite-range or genuinely nonseparable arithmetic coupling before positivity/scalarization**, or couple this positive supplier to an independently forced finite-prime mechanism in a way that simultaneously produces the correct archimedean/global counterterms. Any such extension must still survive the all-integer/generalized-prime controls and must not recover the missing arithmetic by a hand-picked kernel, subtraction, or zero data.