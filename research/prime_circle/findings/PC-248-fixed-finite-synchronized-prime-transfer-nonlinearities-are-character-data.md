# PC-248 — fixed finite synchronized prime-transfer nonlinearities are character data

**Status:** `EXACT-DERIVED` + `PRIOR-ART-CLASSICALIZATION` + `DECISIVE-BOUNDARY` for an explicit escape left open by PC-247. Fix finitely many lower odd primes and let one upper prime `q` vary. Even if the complete centered PC-246 transfer Gram packets at those lower primes are retained simultaneously and then combined by an arbitrary fixed, `q`-independent nonlinear readout, the result still factors through one finite residue quotient. By finite Fourier analysis it is exactly a finite packet of Dirichlet characters modulo the product of the lower primes. Tensor products and other nonlinear couplings can create mixed-conductor characters, but only as ordinary CRT products of the local even characters already present in PC-247.

Consequently the prime-only Dirichlet transform of any such fixed synchronized readout is a finite linear combination of classical Dirichlet prime `L` / prime-zeta-modulo series, hence in `Re(s)>1` a finite combination of logarithms of ordinary Dirichlet `L(ms,psi^m)` factors by the same Euler-product Möbius inversion used in PC-247. This closes fixed finite nonlinear fusion across several lower-prime Gram packets. It does **not** close growing lower moduli, networks involving several independent upper primes, the full rectangular transfer packets before Gram compression, native composite masks, or genuinely infinite-dimensional/joint-limit constructions.

## 1. Start from the exact fixed-base packet decomposition

For distinct primes `p<q`, PC-246 gives the native prime-prime transfer packet `K_{p,q}` and its exact Gram form

\[
K_{p,q}^*K_{p,q}=pq\,I_p-L_{p,h},
\qquad h\equiv q\pmod p,
\tag{1}
\]

where `L_{p,h}` is the weighted path Laplacian with edge weights

\[
w_k(h)=f_p(hk\bmod p),
\qquad
f_p(a)=a(p-a),
\qquad 1\le k<p.
\tag{2}
\]

PC-247 then identifies the residue mean

\[
\overline L_p=\frac{p(p+1)}6\,\Delta_p
\tag{3}
\]

and the centered defect

\[
D_p(h):=L_{p,h}-\overline L_p.
\tag{4}
\]

Let `G_p=(Z/pZ)^x`. With the notation of PC-247, finite multiplicative Fourier inversion gives the exact matrix identity

\[
\boxed{
D_p(h)
=
\sum_{\substack{\chi\bmod p\\
\chi\ne\chi_0,\ \chi(-1)=1}}
\widehat f_p(\chi)\,\chi(h)\,B_{p,\chi}.
}
\tag{5}
\]

For the nonprincipal even characters,

\[
\widehat f_p(\chi)
=\frac{2p}{p-1}L(-1,\overline\chi).
\tag{6}
\]

The point needed here is stronger than the special-value formula. Since `f_p(-a)=f_p(a)`,

\[
\boxed{D_p(-h)=D_p(h).}
\tag{7}
\]

Thus one complete centered matrix at a fixed lower prime sees the upper prime only through the finite signed residue class

\[
[h]\in H_p:=G_p/\{\pm1\}.
\tag{8}
\]

Nothing in the argument below takes a trace, determinant, eigenvalue ordering, or other scalar compression of `D_p(h)`.

## 2. Several fixed lower primes give one finite CRT quotient

Fix distinct odd primes

\[
p_1,\ldots,p_r,
\qquad
M:=\prod_{i=1}^r p_i,
\qquad
P:=\max_i p_i.
\tag{9}
\]

For every prime `q>P`, form the synchronized tuple of complete centered packets

\[
\mathcal D(q)
:=
\bigl(D_{p_1}(q\bmod p_1),\ldots,
D_{p_r}(q\bmod p_r)\bigr).
\tag{10}
\]

The Chinese remainder theorem identifies

\[
G_M:=(\mathbb Z/M\mathbb Z)^\times
\cong
\prod_{i=1}^r G_{p_i}.
\tag{11}
\]

Under this identification let

\[
S_M:=\prod_{i=1}^r\{\pm1\}
\subseteq G_M.
\tag{12}
\]

Equation (7) implies that the entire tuple (10), entry by entry, factors through

\[
\boxed{
H_M:=G_M/S_M
\cong
\prod_{i=1}^r H_{p_i}.
}
\tag{13}
\]

Hence

\[
\boxed{
\mathcal D(q)=\mathcal D(q')
}
\tag{14}
\]

whenever, for each `i`,

\[
q'\equiv \varepsilon_i q\pmod{p_i},
\qquad \varepsilon_i\in\{\pm1\}.
\tag{15}
\]

This is an exact information quotient, not an asymptotic statement. In particular the simultaneous collection of several lower-prime matrices does not create a continuous or growing variable while the lower-prime set is fixed: it is one function on the finite abelian group `H_M`.

The prime condition on `q` is not used in (13)--(15) after the PC-246 packet has been derived. It only specifies which residue classes are sampled by the original upper-shell family.

## 3. Arbitrary fixed nonlinear fusion cannot leave the finite character algebra

Let `V` be any fixed complex vector space and let

\[
F:\prod_{i=1}^r \operatorname{Mat}_{p_i}(\mathbb C)\longrightarrow V
\tag{16}
\]

be any fixed map defined on the finite image of (10). No linearity, polynomiality, commutativity, analyticity, or spectral assumption is required. Define

\[
A_F(q):=F(\mathcal D(q)).
\tag{17}
\]

Because (10) factors through `H_M`, so does (17). Fourier analysis on the finite abelian group `H_M` therefore gives unique coefficients `C_psi in V` such that

\[
\boxed{
A_F(q)=\sum_{\psi\in\widehat H_M}C_\psi\,\psi(q).
}
\tag{18}
\]

Explicitly,

\[
C_\psi
=\frac1{|H_M|}
\sum_{x\in H_M}A_F(x)\,\overline{\psi(x)}.
\tag{19}
\]

Via (11), every `psi in widehat H_M` is an ordinary Dirichlet character modulo `M` whose local component modulo each `p_i` is even:

\[
\psi_i(-1)=1
\qquad(1\le i\le r).
\tag{20}
\]

Equation (18) is the relevant ceiling. It covers entrywise nonlinearities, tensor products, fixed block embeddings followed by noncommuting matrix words, traces of such words, determinants, fixed rational functions wherever defined, spectral statistics determined solely by the matrices, and any other `q`-independent readout of the fixed packet tuple. Such a readout may rearrange or mix the residue information arbitrarily, but it cannot manufacture information outside the finite character algebra of `H_M`.

The statement is deliberately about a **fixed** readout. If coefficients, embeddings, matrix sizes, or the rule `F` themselves depend on the varying upper prime `q`, that extra dependence is new input and is not covered by (18).

## 4. Multilinear coupling does create mixed conductors, but only by CRT character multiplication

For the most natural nonlinear candidate, keep the full tensor product before contraction. Substituting (5) at every lower prime gives

\[
\begin{aligned}
\bigotimes_{i=1}^r D_{p_i}(q)
={}&
\sum_{\chi_1,\ldots,\chi_r}
\left(
\prod_{i=1}^r\widehat f_{p_i}(\chi_i)
\right)
\left(
\bigotimes_{i=1}^r B_{p_i,\chi_i}
\right)
\prod_{i=1}^r\chi_i(q),
\end{aligned}
\tag{21}
\]

where every `chi_i` is nonprincipal and even modulo `p_i`. By CRT,

\[
\psi_{\boldsymbol\chi}(n)
:=\prod_{i=1}^r\chi_i(n)
\tag{22}
\]

is simply a Dirichlet character modulo `M`. Thus a nonlinear product **can** produce a character whose conductor involves several lower primes. That mixed label is real, but it is exactly the ordinary product character forced by finite-group representation theory; there is no additional cocycle, phase, or path memory.

More general polynomial words allow repeated local characters and principal channels generated by products such as `chi_i^k`, but still remain inside `widehat H_M`. Arbitrary nonlinear `F` in (16) can in principle use the whole character group of `H_M`; equation (18) shows that this is already the maximal possible information content.

A small exact control illustrates the quotient. For `p=5`, PC-247 gives

\[
D_5(h)=-\chi_5(h)B_{5,\chi_5},
\tag{23}
\]

with `chi_5` the quadratic character. For the pair `(5,7)`, the synchronized tuple therefore factors through

\[
H_{35}\cong
(G_5/\{\pm1\})\times(G_7/\{\pm1\}),
\qquad |H_{35}|=2\cdot3=6.
\tag{24}
\]

No matter how nonlinearly the two complete matrices are combined by a fixed rule, the output has at most those six residue states and hence six character channels. Checking (15) modulo `5` and `7` is an immediate finite falsification test.

## 5. Prime-only analytic aggregation is a finite combination of classical Dirichlet prime L-functions

Assume now that `V` is finite-dimensional or normed. Since (17) takes only finitely many values, for `Re(s)>1` the prime-only Dirichlet transform converges absolutely:

\[
\mathcal A_F(s)
:=
\sum_{\substack{q>P\\q\ \mathrm{prime}}}
\frac{A_F(q)}{q^s}.
\tag{25}
\]

Using (18),

\[
\boxed{
\mathcal A_F(s)
=
\sum_{\psi\in\widehat H_M}
C_\psi\,P_{\psi,>P}(s),
}
\tag{26}
\]

where

\[
P_{\psi,>P}(s)
:=
\sum_{\substack{q>P\\q\ \mathrm{prime}}}
\frac{\psi(q)}{q^s}.
\tag{27}
\]

Removing the cutoff changes this only by a finite Dirichlet polynomial. For

\[
P_\psi(s):=\sum_{q\ \mathrm{prime}}\frac{\psi(q)}{q^s},
\tag{28}
\]

the Euler product of the ordinary Dirichlet `L`-function gives, exactly as in PC-247,

\[
\log L(s,\psi)
=
\sum_{m\ge1}\frac1m P_{\psi^m}(ms),
\qquad \Re(s)>1,
\tag{29}
\]

and Möbius inversion in the exponent gives

\[
\boxed{
P_\psi(s)
=
\sum_{m\ge1}\frac{\mu(m)}m
\log L(ms,\psi^m),
\qquad \Re(s)>1.
}
\tag{30}
\]

Thus even after nonlinear mixing has generated composite-modulus character channels, the all-upper-prime analytic variable is the established Dirichlet prime-`L` package. On continuation, wherever branches are chosen, its singularities can only be inherited from the poles and zeros of the classical factors in (30), up to cancellations among the finite channels. Zeros of an arbitrarily chosen linear combination in (26) may of course occur elsewhere, but they are not a source-forced Euler product, functional equation, or independent zero divisor; changing `F` can change them arbitrarily within the same finite residue algebra.

In particular, the principal channel that a nonlinear readout may generate uses

\[
L(s,\psi_0)
=\zeta(s)\prod_{p\mid M}(1-p^{-s}).
\tag{31}
\]

So the Riemann zeta function can re-enter this construction, but only as the ordinary principal Dirichlet-character factor. That is precisely the kind of classical reparameterization excluded by the Prime-Circle research mandate as progress by itself.

## 6. Information-gain and matched-control interpretation

PC-247 deliberately left `nonlinear products coupling different lower primes` outside its fixed-base linear theorem. Equations (13) and (18) now close that loophole for every **fixed finite synchronized family of centered Gram packets**. Nonlinearity can increase the visible character set from separate local channels to product characters modulo `M`, but it cannot increase the underlying state space beyond the finite CRT quotient already determined by signed residues.

This also supplies a stronger control than testing one chosen invariant. Once the lower primes are fixed, two upper indices satisfying (15) give identical complete input matrices. Therefore **every** fixed readout `F` gives the same answer on them. No trace/determinant/spectrum can recover information that the entire tuple itself does not contain.

For prime summation, the only remaining distinction is which residue classes are visited by prime indices and with what frequency. Character decomposition turns precisely that sampling problem into the classical distribution of primes against Dirichlet characters modulo `M`. A surrogate sequence with the same residue-class sampling produces the same packet-valued aggregate. This is a sampling control, not a claim that a composite upper cyclotomic shell has the same native transfer packet as a prime shell.

## 7. Prior-art and novelty audit

No novelty is claimed for the Chinese remainder theorem, characters of finite abelian groups, Fourier inversion on a finite character group, products of Dirichlet characters, Euler products, or Möbius inversion. `research/prime_circle/SOURCES.md` already anchors finite-abelian character/convolution methods and the standard Dirichlet-series identities used throughout this line, while PC-247 records the exact prime-character Euler-product reduction (29)--(30) for the immediately preceding packet family.

A targeted external search over finite abelian Fourier decomposition, CRT factorization of Dirichlet characters, and prime-restricted character Dirichlet series found the expected classical framework and terminology; no prior work was located for the project-specific statement that the PC-246 synchronized Gram packet tuple factors through (13). The negative conclusion does not rely on an absence-of-literature claim: (13), (18), and (26) are exact algebraic reductions.

The only project-local content worth recording is therefore the **closure theorem**: the apparently open nonlinear multi-base escape from PC-247 does generate mixed characters, but these are exactly the classical CRT products and no larger information carrier survives at fixed finite lower modulus.

## 8. Boundary of the theorem

The following chain is closed:

\[
\boxed{
\text{fixed finite lower primes }p_1,\ldots,p_r
\longrightarrow
\{D_{p_i}(q)\}_{i=1}^r
\longrightarrow
\text{arbitrary fixed synchronized nonlinear readout}
\longrightarrow
\text{new all-scale RH carrier}.
}
\tag{32}
\]

The theorem does **not** close several materially different possibilities. The lower-prime set may grow so that `M` itself tends to infinity; several independent upper primes may be coupled before contraction; the rectangular `K_{p,q}` packets may be retained with their changing `q`-dimensional orientation rather than replaced by `K^*K`; native composite cyclotomic masks may introduce coefficient data not present in prime all-one masks; or an infinite-dimensional/source-forced topology may be taken before the fixed-modulus character quotient. Nonlinear/off-circle/global-uniformization structures outside this transfer family are also untouched.

Accordingly the next packet-level survivor must use **growing modulus or genuinely relational multi-upper-prime information before fixed finite residue compression**. Repeating fixed lower bases and making the final matrix algebra more nonlinear is no longer a distinct escape.

## Falsification checks

The finding is exact and has several short checks. First verify PC-247 equation (5) and hence `D_p(-h)=D_p(h)`. For any fixed lower-prime list, enumerate `G_M` and confirm directly that the complete synchronized tuple is constant on the `S_M` cosets in (13). Then choose an arbitrary nonlinear table `F` on those tuples and compute the finite Fourier coefficients (19); inversion must reproduce every table value exactly and coefficients outside the locally-even character group must vanish. For `(p_1,p_2)=(5,7)`, there must be at most six distinct tuple values as in (24). For a multilinear test, expand the tensor product and verify (21)--(22) directly. Finally substitute (29) into the right side of (30): the coefficient of `P_{psi^r}(rs)` is `(1/r) sum_{m|r} mu(m)`, leaving only `r=1`. Failure of any one of these exact reductions changes the claimed boundary; otherwise every fixed finite synchronized nonlinear Gram-packet fusion is confined to classical Dirichlet-character data.