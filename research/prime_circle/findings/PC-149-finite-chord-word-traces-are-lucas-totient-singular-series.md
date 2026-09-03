# PC-149 — finite chord-word traces are Lucas-totient singular-series data

**Status:** `EXACT-DERIVED` + `LITERATURE+DERIVED` + `CLASSICAL-IDENTITY` + `DECISIVE-BOUNDARY`. PC-147 proves that the isolated primorial inverse-square top band is uniformly approximable in operator norm by finite chord-radius truncations, while PC-148 shows that the exact gap-two backbone has a completely flat CRT refinement correspondence. A natural surviving question is whether keeping the **noncommutative finite-local operator algebra before diagonalization** can recover arithmetic interaction that is lost by the single matching skeleton.

For every fixed collection of chord offsets, the answer is sharply limited. Compress additive translations to the primitive residues. Under coprime CRT every compressed translation factors as an exact tensor product, so every ordered word factors prime-by-prime before taking a trace. The trace of a closed word is then exactly the number of translates of one finite offset constellation that remain units modulo `n`: a classical Lucas/generalized-Schemmel totient. Along primorials its normalized value is the Hardy--Littlewood singular-series local density times the corresponding Mertens power.

Consequently **every fixed polynomial moment of every fixed-radius primitive-shell chord operator**, including the inverse-square truncated Laplacians used in PC-145--PC-147, is a finite linear combination of classical reduced-residue tuple products with deterministic chord weights. Noncommutativity of the finite-local primitive shifts does not by itself create a new zeta-zero-sensitive moment hierarchy. What remains outside the theorem is genuinely non-polynomial spectral data, word length or chord radius growing with the conductor, and cross-level organization of the actual spectral projectors rather than fixed local words.

## 1. Primitive compressed translations form an exact CRT tensor system

Let

\[
U_n=(\mathbb Z/n\mathbb Z)^\times,
\qquad
\mathcal H_n=\ell^2(U_n).
\]

On `\ell^2(\mathbb Z/n\mathbb Z)` let `\tau_h^{(n)}` be translation by `h`, and let `P_n` be the coordinate projection onto `U_n`. Restrict the compressed translation

\[
\boxed{
T_{n,h}:=P_n\tau_h^{(n)}P_n\big|_{\mathcal H_n}.
}
\tag{1}
\]

Equivalently, in the standard basis it is the partial permutation that moves a primitive residue by `h` only when the translated residue is still primitive. With the convention

\[
T_{n,h}e_a=
\begin{cases}
e_{a+h},&a+h\in U_n,\\0,&a+h\notin U_n,
\end{cases}
\]

one has `T_{n,h}^*=T_{n,-h}`.

If `(n,m)=1`, CRT gives a canonical unitary identification

\[
C_{n,m}:\mathcal H_{nm}\longrightarrow\mathcal H_n\otimes\mathcal H_m,
\qquad
e_a\longmapsto e_{a\bmod n}\otimes e_{a\bmod m}.
\tag{2}
\]

Addition by the same integer `h` acts componentwise under CRT, and primitivity modulo `nm` is exactly primitivity in both factors. Hence

\[
\boxed{
C_{n,m}T_{nm,h}C_{n,m}^{-1}
=T_{n,h}\otimes T_{m,h}.
}
\tag{3}
\]

This holds for every integer offset `h`; no small-offset, prime, squarefree, asymptotic, or spectral assumption is required.

For an ordered word

\[
w=(h_1,\ldots,h_k),
\qquad
T_{n,w}:=T_{n,h_k}\cdots T_{n,h_1},
\tag{4}
\]

equation (3) multiplies componentwise to give

\[
\boxed{
C_{n,m}T_{nm,w}C_{n,m}^{-1}
=T_{n,w}\otimes T_{m,w}.
}
\tag{5}
\]

Therefore the trace of every word is multiplicative on coprime moduli:

\[
\boxed{
\operatorname{Tr}T_{nm,w}
=\operatorname{Tr}T_{n,w}\,\operatorname{Tr}T_{m,w}.
}
\tag{6}
\]

The generators `T_{n,h}` generally **do not commute** after primitive compression; (5) is therefore a factorization of the full ordered-word data, not a consequence of first diagonalizing a commutative algebra.

## 2. A closed word is exactly a reduced-residue tuple count

Put

\[
s_0=0,
\qquad
s_j=h_1+\cdots+h_j
\quad(1\le j\le k),
\tag{7}
\]

and let

\[
A_w:=\{s_0,s_1,\ldots,s_{k-1}\}\subset\mathbb Z
\tag{8}
\]

with repeated partial sums removed as a set. Starting from `a\in U_n`, the word survives exactly when every intermediate residue `a+s_j` is a unit. It returns to the starting basis vector exactly when

\[
s_k\equiv0\pmod n.
\tag{9}
\]

Thus if (9) fails,

\[
\operatorname{Tr}T_{n,w}=0.
\tag{10}
\]

If (9) holds, the diagonal entries count precisely the translates of `A_w` avoiding every prime divisor of `n`:

\[
\boxed{
\operatorname{Tr}T_{n,w}
=\#\{a\bmod n:(a+s,n)=1\text{ for every }s\in A_w\}.
}
\tag{11}
\]

For a prime power `p^e\parallel n`, let

\[
\nu_p(A_w):=
\#\{s\bmod p:s\in A_w\}.
\tag{12}
\]

Exactly `\nu_p(A_w)` residue classes of `a mod p` are forbidden. Every allowed class has `p^{e-1}` lifts modulo `p^e`, so CRT gives the exact product

\[
\boxed{
\operatorname{Tr}T_{n,w}
=
\prod_{p^e\parallel n}
p^{e-1}\bigl(p-\nu_p(A_w)\bigr)
}
\tag{13}
\]

whenever the word closes modulo `n`.

This arithmetic function is classical. Pabhapote--Laohakosol, **Combinatorial Aspects of the Generalized Euler's Totient**, *International Journal of Mathematics and Mathematical Sciences* 2010, Article 648165, DOI `10.1155/2010/648165`, records Lucas's totient for arbitrary fixed offsets: it counts translates for which all specified shifts are coprime to `n`, with the local factor determined by the number of distinct occupied classes modulo each prime. Their Schemmel functions are the consecutive-offset specialization. Thus (13) is not a new arithmetic counting law; the Prime-Circle content is the identification of **all finite ordered compressed-chord traces** with this classical tuple-count class.

As finite checks at `n=30`, the closed word `(4,-4)` has `A_w={0,4}` and (13) gives

\[
(2-1)(3-2)(5-2)=3,
\]

while `(4,2,-6)` has `A_w={0,4,6}` and gives

\[
(2-1)(3-2)(5-3)=2.
\]

Direct primitive-residue enumeration gives exactly the same traces.

## 3. Primorial traces are Hardy--Littlewood singular-series densities

Now let

\[
N_x=\prod_{p\le x}p
\]

and fix an **integer-closed** word, `s_k=0`, independently of `x`. Write

\[
r:=|A_w|.
\]

Dividing (13) by `\varphi(N_x)` gives

\[
\boxed{
\frac{\operatorname{Tr}T_{N_x,w}}{\varphi(N_x)}
=
\prod_{p\le x}
\frac{p-\nu_p(A_w)}{p-1}.
}
\tag{14}
\]

If `A_w` occupies every residue class modulo some prime, the word is locally inadmissible and the right side is exactly zero once that prime enters the primorial. Otherwise define the standard Hardy--Littlewood singular series of the finite offset set

\[
\mathfrak S(A_w)
:=
\prod_p
\frac{1-\nu_p(A_w)/p}{(1-1/p)^r}.
\tag{15}
\]

For all sufficiently large primes the integer offsets are distinct modulo `p`, so `\nu_p(A_w)=r` and the normalized local factor in (15) is `1+O(p^{-2})`. Hence the product converges to a positive constant for an admissible pattern. Rewriting (14) as

\[
\prod_{p\le x}
\frac{1-\nu_p(A_w)/p}{(1-1/p)^r}
\left(\prod_{p\le x}(1-1/p)\right)^{r-1}
\]

and applying Mertens' product theorem yields

\[
\boxed{
\frac{\operatorname{Tr}T_{N_x,w}}{\varphi(N_x)}
\sim
\frac{e^{-\gamma(r-1)}\mathfrak S(A_w)}{(\log x)^{r-1}}.
}
\tag{16}
\]

Thus every fixed closed word has one of two asymptotic fates: an exact local obstruction kills it, or its density is a classical singular-series constant times a deterministic Mertens power.

This places the PC-143/PC-144 three-point phenomenon in a larger exact hierarchy. Their conditional extra-neighbor density divides a three-point count by the already-imposed gap-two two-point count, so the absolute `r=3` and `r=2` Mertens powers differ by one factor `1/log x`, precisely the scale found in PC-144.

## 4. Every fixed-radius polynomial chord moment lies in this classical class

The finite-local inverse-square operator is generated by the same partial translations. For a fixed positive chord cutoff `H`, let

\[
w_h(n)=\frac1{4\sin^2(\pi h/n)},
\qquad 1\le h\le H,
\tag{17}
\]

and assume `2H<n` so the signed offsets are unambiguous. Define the neighbor projections

\[
D_{n,h}:=T_{n,-h}T_{n,h},
\qquad
D_{n,-h}:=T_{n,h}T_{n,-h}.
\tag{18}
\]

The primitive-shell Laplacian contributed by chord offset `h` is

\[
L_{n,h}
=w_h(n)
\bigl(D_{n,h}+D_{n,-h}-T_{n,h}-T_{n,-h}\bigr),
\tag{19}
\]

and the radius-`H` truncation is

\[
L_n^{(H)}=\sum_{h=1}^H L_{n,h}.
\tag{20}
\]

This includes the finite-window operators of PC-145--PC-147, modulo the already-separated gap-two matching convention used there.

For every fixed moment order `k`, expanding `(L_n^{(H)})^k` produces only finitely many ordered words in the generators `T_{n,\pm h}`. Equations (10)--(13) therefore give an **exact finite formula**

\[
\boxed{
\operatorname{Tr}\bigl((L_n^{(H)})^k\bigr)
=
\sum_{w\in\mathcal W_{H,k}}
 c_w(n)
\prod_{p^e\parallel n}
p^{e-1}\bigl(p-\nu_p(A_w)\bigr),
}
\tag{21}
\]

where `\mathcal W_{H,k}` is a finite set of closed partial-translation words and every coefficient `c_w(n)` is an explicit signed product of the geometric chord weights (17). The exact list depends only on `H`, `k`, and the elementary Laplacian expansion, not on any hidden arithmetic choice.

Along primorials, since for fixed `h`

\[
\frac{w_h(N_x)}{N_x^2}
\longrightarrow
\frac1{4\pi^2h^2},
\tag{22}
\]

every normalized fixed moment

\[
\frac{
\operatorname{Tr}((L_{N_x}^{(H)})^k)
}{
\varphi(N_x)N_x^{2k}
}
\tag{23}
\]

is a finite linear combination of the classical singular-series/Mertens terms in (16), with deterministic constants from the chord lengths. Cancellations may alter which Mertens power is leading, but cannot introduce a new arithmetic ingredient: each summand is already a Lucas-totient local product.

The same conclusion applies to any fixed noncommutative polynomial in finitely many primitive compressed chord shifts, not only to powers of a self-adjoint Laplacian. Keeping operator order before tracing therefore does not evade the reduction.

## 5. Cross-level refinement of every fixed word is CRT-flat

Equation (5) also extends the cross-level conclusion of PC-148 beyond the single gap-two matching. For pairwise coprime factors `n,p,q`, the two canonical CRT associations

\[
\mathcal H_{npq}
\cong
\mathcal H_n\otimes\mathcal H_p\otimes\mathcal H_q
\]

agree up to the canonical permutation of tensor factors, and for every fixed word

\[
\boxed{
T_{npq,w}
\cong
T_{n,w}\otimes T_{p,w}\otimes T_{q,w}.
}
\tag{24}
\]

Thus adjoining `p` and then `q`, or `q` and then `p`, cannot generate an order-dependent defect inside the fixed-word incidence algebra. For geometric chord operators the weights `w_h(n)` depend on the final circle size, but that dependence is an endpoint scalar attached to each offset channel; it does not alter the associative CRT factorization (24) or create a prime-order cocycle.

This does **not** say that spectral projectors of sums of many words factor as tensor products. Spectral projection is nonlinear and the chord weights at different levels are not a common scalar rescaling. The theorem instead removes a more basic possibility: any proposed refinement curvature that already appears in a fixed ordered local incidence word is impossible, because the exact word itself is canonically factorized before spectral interpretation.

## 6. Prior-art and novelty audit

The arithmetic side is classical. The exact finite count (13) is the arbitrary-offset Lucas-totient product recorded by Pabhapote--Laohakosol; the consecutive special cases are Schemmel totients. The primorial normalization (15)--(16) is precisely the local-density product of the Hardy--Littlewood finite-tuple singular series combined with Mertens' theorem. PC-143 already places the corresponding reduced-residue tuple geometry next to Montgomery--Vaughan and Aryan's work on reduced residues and `k`-tuples.

The operator side uses only standard facts: traces of products of partial permutation matrices count closed admissible walks, and CRT identifies units modulo coprime products with products of local unit sets. Directed searches across reduced-residue tuple counts, generalized totients, unitary-Cayley/direct-product decompositions, compressed translations on unit sets, and graph closed-walk moments did not locate this exact Prime-Circle compressed-chord formulation. That absence is not a novelty claim. The durable contribution is a **classification boundary** for the current research line: the entire fixed local noncommutative moment algebra reduces to known local-density arithmetic.

The RH audit is correspondingly negative. No complex spectral parameter, analytic continuation, gamma factor, functional equation, or critical-line involution appears in (1)--(24). Taking a Dirichlet or Mellin transform of the multiplicative word counts afterward would import the same sort of external transform already excluded elsewhere in the line; it would not make the fixed local word itself a new RH mechanism.

## 7. Boundary and falsification surface

1. For any coprime `n,m` and offset `h`, direct CRT reindexing must make `T_{nm,h}` exactly equal to `T_{n,h}\otimes T_{m,h}`. One counterexample falsifies the tensor claim.
2. For any word `w`, if its total displacement is nonzero modulo `n`, its trace must vanish. If it closes, direct enumeration must agree with (13).
3. Repeated partial sums must be counted only once in `A_w`; modulo a prime, further collisions are handled by `\nu_p(A_w)`. Omitting either collision rule gives incorrect local factors.
4. For an admissible fixed integer pattern, the normalized primorial trace must obey the Mertens exponent `r-1` in (16); an inadmissible pattern must become exactly zero once a blocking prime is included.
5. Every fixed-radius, fixed-degree polynomial observable expands into finitely many such words. A proposed counterexample must therefore identify a term not generated by the compressed translations or a dependence whose degree/radius grows with the conductor.
6. The theorem does **not** determine the full spectrum, individual eigenvalue spacings, spectral projectors, Fredholm determinants with degree growing with dimension, or limits where chord radius/word length grows with `N_x`. In particular it does not prove that the residual top-band transport `Q_{N_x}-P_{N_x}` left open by PC-148 is flat.

The surviving finite-local frontier is therefore narrower: new information cannot come from any fixed polynomial trace of bounded chord interactions. It must use a genuinely non-polynomial spectral observable, growing-complexity local geometry, or cross-level organization that is not already visible in one fixed CRT-factorized word.
